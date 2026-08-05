from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import seguridad

class CategoriaEntrada(BaseModel):
    nombre: str

router = APIRouter(prefix="/categorias", tags=["Categorias"])

# GET público
@router.get("")
def listar_categorias():
    return [{"id": 1, "nombre": "Electrónica"}]

# POST protegido (requiere autenticación)
@router.post("", status_code=201)
def crear_categoria(
    datos: CategoriaEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    return {
        "mensaje": "Categoría creada",
        "categoria": {"id": 2, "nombre": datos.nombre},
        "creada_por": usuario["username"]
    }

# PUT protegido (requiere autenticación)
@router.put("/{categoria_id}")
def actualizar_categoria(
    categoria_id: int,
    datos: CategoriaEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    return {
        "mensaje": f"Categoría {categoria_id} actualizada",
        "actualizada_por": usuario["username"]
    }

# DELETE protegido (requiere rol admin)
@router.delete("/{categoria_id}")
def eliminar_categoria(
    categoria_id: int,
    admin: dict = Depends(seguridad.requerir_admin)
):
    return {
        "mensaje": f"Categoría {categoria_id} eliminada",
        "eliminada_por": admin["username"]
    }