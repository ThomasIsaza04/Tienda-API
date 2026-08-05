from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import seguridad

class UsuarioActualizar(BaseModel):
    nombre: str

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# --- ENDPOINTS PROTEGIDOS ---

# Listar todos los usuarios (Exclusivo Administradores)
@router.get("", status_code=200)
def listar_usuarios(admin: dict = Depends(seguridad.requerir_admin)):
    # Retornamos los usuarios omitiendo o limpiando las contraseñas
    usuarios_limpios = [
        {"username": u["username"], "nombre": u["nombre"], "rol": u["rol"]}
        for u in seguridad.usuarios
    ]
    return usuarios_limpios

# Consultar un usuario por su Username (Exclusivo Administradores)
@router.get("/{username}", status_code=200)
def obtener_usuario(username: str, admin: dict = Depends(seguridad.requerir_admin)):
    u = seguridad.buscar_usuario(username)
    if u:
        return {"username": u["username"], "nombre": u["nombre"], "rol": u["rol"]}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Actualizar datos del usuario autenticado
@router.put("/perfil", status_code=200)
def actualizar_perfil(
    datos: UsuarioActualizar,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    usuario["nombre"] = datos.nombre
    return {
        "mensaje": "Perfil actualizado exitosamente",
        "usuario": {"username": usuario["username"], "nombre": usuario["nombre"], "rol": usuario["rol"]}
    }

# Eliminar usuario por username (Exclusivo Administradores)
@router.delete("/{username}", status_code=200)
def eliminar_usuario(username: str, admin: dict = Depends(seguridad.requerir_admin)):
    for i, u in enumerate(seguridad.usuarios):
        if u["username"] == username:
            seguridad.usuarios.pop(i)
            return {"mensaje": f"Usuario '{username}' eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")