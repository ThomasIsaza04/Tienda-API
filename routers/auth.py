from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import seguridad

# Crear el router para este módulo
router = APIRouter(prefix="/auth", tags=["Autenticacion"])

class UsuarioRegistro(BaseModel):
    username: str
    nombre: str
    password: str

# LOGIN: Entrega el token de acceso JWT
@router.post("/login")
def login(datos: OAuth2PasswordRequestForm = Depends()):
    usuario = seguridad.buscar_usuario(datos.username)
    if usuario is None or not seguridad.verificar_password(datos.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    token = seguridad.crear_token(usuario["username"])
    return {"access_token": token, "token_type": "bearer"}

# QUIEN SOY: Endpoint protegido que retorna la identidad actual
@router.get("/yo")
def quien_soy(usuario: dict = Depends(seguridad.obtener_usuario_actual)):
    return {"username": usuario["username"], "rol": usuario["rol"]}

# REGISTRO: Permite registrar nuevos usuarios
@router.post("/registro", status_code=201)
def registrar_usuario(datos: UsuarioRegistro):
    if seguridad.buscar_usuario(datos.username):
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    nuevo_usuario = {
        "username": datos.username,
        "nombre": datos.nombre,
        "password": seguridad.hashear_password(datos.password),
        "rol": "cliente"
    }
    seguridad.usuarios.append(nuevo_usuario)
    return {"mensaje": "Usuario registrado exitosamente", "username": datos.username}