from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import seguridad

class ProductoEntrada(BaseModel):
    nombre: str
    precio: float
    categoria_id: int

router = APIRouter(prefix="/productos", tags=["Productos"])

# Base de datos en memoria para pruebas
productos_db = [
    {"id": 1, "nombre": "Teclado", "precio": 50.0, "categoria_id": 1}
]

# --- ENDPOINTS PÚBLICOS ---

# GET público - Listar todos
@router.get("")
def listar_productos():
    return productos_db

# GET público - Consultar por ID
@router.get("/{producto_id}")
def obtener_producto(producto_id: int):
    for prod in productos_db:
        if prod["id"] == producto_id:
            return prod
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# --- ENDPOINTS PROTEGIDOS ---

# POST protegido (cualquier usuario autenticado)
@router.post("", status_code=201)
def crear_producto(
    datos: ProductoEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    nuevo = {"id": len(productos_db) + 1, **datos.model_dump()}
    productos_db.append(nuevo)
    return {
        "mensaje": "Producto creado",
        "producto": nuevo,
        "creado_por": usuario["username"]
    }

# PUT protegido (cualquier usuario autenticado)
@router.put("/{producto_id}")
def actualizar_producto(
    producto_id: int,
    datos: ProductoEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    for prod in productos_db:
        if prod["id"] == producto_id:
            prod["nombre"] = datos.nombre
            prod["precio"] = datos.precio
            prod["categoria_id"] = datos.categoria_id
            return {
                "mensaje": f"Producto {producto_id} actualizado",
                "actualizado_por": usuario["username"]
            }
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# DELETE protegido (solo admin)
@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    admin: dict = Depends(seguridad.requerir_admin)
):
    for i, prod in enumerate(productos_db):
        if prod["id"] == producto_id:
            productos_db.pop(i)
            return {
                "mensaje": f"Producto {producto_id} eliminado",
                "eliminado_por": admin["username"]
            }
    raise HTTPException(status_code=404, detail="Producto no encontrado")