from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import seguridad

# Asumiendo tu estructura de modelos de la Guía 02:
class ProductoEntrada(BaseModel):
    nombre: str
    precio: float
    categoria_id: int

router = APIRouter(prefix="/productos", tags=["Productos"])

# GET público
@router.get("")
def listar_productos():
    return [{"id": 1, "nombre": "Teclado", "precio": 50.0}]

# POST protegido (cualquier usuario autenticado)
@router.post("", status_code=201)
def crear_producto(
    datos: ProductoEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    nuevo = {"id": 2, **datos.model_dump()}
    return {
        "mensaje": "Producto creado",
        "producto": nuevo,
        "creado_por": usuario["username"]
    }

# PUT protegido (cualquier usuario autenticado - Ejercicio 4)
@router.put("/{producto_id}")
def actualizar_producto(
    producto_id: int,
    datos: ProductoEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    return {
        "mensaje": f"Producto {producto_id} actualizado",
        "actualizado_por": usuario["username"]
    }

# DELETE protegido (solo admin)
@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    admin: dict = Depends(seguridad.requerir_admin)
):
    return {
        "mensaje": f"Producto {producto_id} eliminado",
        "eliminado_por": admin["username"]
    }