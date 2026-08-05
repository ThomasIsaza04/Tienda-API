from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import seguridad

class CategoriaEntrada(BaseModel):
    nombre: str

router = APIRouter(prefix="/categorias", tags=["Categorias"])

# Lista de prueba en memoria
categorias_db = [
    {"id": 1, "nombre": "Electrónica"}
]

# --- ENDPOINTS PÚBLICOS ---

# Listar todas las categorías
@router.get("")
def listar_categorias():
    return categorias_db

# Obtener categoría por ID
@router.get("/{categoria_id}")
def obtener_categoria(categoria_id: int):
    for cat in categorias_db:
        if cat["id"] == categoria_id:
            return cat
    raise HTTPException(status_code=404, detail="Categoría no encontrada")

# --- ENDPOINTS PROTEGIDOS ---

# POST protegido (requiere autenticación)
@router.post("", status_code=201)
def crear_categoria(
    datos: CategoriaEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    nueva = {"id": len(categorias_db) + 1, "nombre": datos.nombre}
    categorias_db.append(nueva)
    return {
        "mensaje": "Categoría creada",
        "categoria": nueva,
        "creada_por": usuario["username"]
    }

# PUT protegido (requiere autenticación)
@router.put("/{categoria_id}")
def actualizar_categoria(
    categoria_id: int,
    datos: CategoriaEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    for cat in categorias_db:
        if cat["id"] == categoria_id:
            cat["nombre"] = datos.nombre
            return {
                "mensaje": f"Categoría {categoria_id} actualizada",
                "actualizada_por": usuario["username"]
            }
    raise HTTPException(status_code=404, detail="Categoría no encontrada")

# DELETE protegido (requiere rol admin)
@router.delete("/{categoria_id}")
def eliminar_categoria(
    categoria_id: int,
    admin: dict = Depends(seguridad.requerir_admin)
):
    for i, cat in enumerate(categorias_db):
        if cat["id"] == categoria_id:
            categorias_db.pop(i)
            return {
                "mensaje": f"Categoría {categoria_id} eliminada",
                "eliminada_por": admin["username"]
            }
    raise HTTPException(status_code=404, detail="Categoría no encontrada")