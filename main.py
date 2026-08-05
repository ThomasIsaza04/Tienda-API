from fastapi import FastAPI
from routers import auth, productos, categorias, usuarios, pedidos

app = FastAPI(
    title="API E-Commerce Segura",
    description="API REST modularizada con autenticación OAuth2 / JWT y control de acceso por roles (RBAC).",
    version="1.0.0"
)

# Registro de routers
app.include_router(auth.router)
app.include_router(productos.router)
app.include_router(categorias.router)
app.include_router(usuarios.router)
app.include_router(pedidos.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API E-Commerce Segura funcionando correctamente.",
        "documentacion": "Visita /docs para probar los endpoints interactivos con Swagger UI."
    }