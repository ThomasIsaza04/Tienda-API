from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Configuración JWT
SECRET_KEY = "clave-super-secreta-de-mas-de-32-caracteres-cambieme"
ALGORITMO = "HS256"
MINUTOS_EXPIRACION = 30

# Hashing de contraseñas con bcrypt directamente
def hashear_password(password: str) -> str:
    hasheado = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hasheado.decode()

def verificar_password(plano: str, hasheado: str) -> bool:
    return bcrypt.checkpw(plano.encode(), hasheado.encode())

# Usuarios de prueba (contraseñas hasheadas en memoria)
usuarios = [
    {
        "username": "admin",
        "nombre": "Administrador",
        "password": hashear_password("admin123"),
        "rol": "admin"
    },
    {
        "username": "ana",
        "nombre": "Ana Cliente",
        "password": hashear_password("ana123"),
        "rol": "cliente"
    }
]

def buscar_usuario(username: str):
    for usuario in usuarios:
        if usuario["username"] == username:
            return usuario
    return None

# Crear Token JWT
def crear_token(username: str) -> str:
    expira = datetime.now(timezone.utc) + timedelta(minutes=MINUTOS_EXPIRACION)
    return jwt.encode({"sub": username, "exp": expira}, SECRET_KEY, algorithm=ALGORITMO)

# Esquema OAuth2 para FastAPI /docs
oauth2_esquema = OAuth2PasswordBearer(tokenUrl="auth/login")

# Dependencia: Valida el token JWT (Devuelve 401 si falla)
def obtener_usuario_actual(token: str = Depends(oauth2_esquema)):
    error = HTTPException(
        status_code=401,
        detail="Token invalido",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        username = datos.get("sub")
        if username is None:
            raise error
    except jwt.PyJWTError:
        raise error
        
    usuario = buscar_usuario(username)
    if usuario is None:
        raise error
    return usuario

# Dependencia: Exige rol administrador (Devuelve 403 si falla)
def requerir_admin(usuario: dict = Depends(obtener_usuario_actual)):
    if usuario["rol"] != "admin":
        raise HTTPException(status_code=403, detail="Requiere rol de administrador")
    return usuario