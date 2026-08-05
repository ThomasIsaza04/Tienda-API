from fastapi import FastAPI
from routers import auth, productos, categorias

# Inicialización de la aplicación FastAPI con metadatos para Swagger
app = FastAPI(
    title="API E-Commerce Segura",
    description="API REST modularizada con autenticación OAuth2 / JWT y control de acceso por roles (RBAC).",
    version="1.0.0"
)

# Registro de routers para los módulos del sistema
app.include_router(auth.router)
app.include_router(productos.router)
app.include_router(categorias.router)

# Endpoint raíz de bienvenida
@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API E-Commerce Segura funcionando correctamente.",
        "documentacion": "Visita /docs para probar los endpoints interactivos con Swagger UI."
    }