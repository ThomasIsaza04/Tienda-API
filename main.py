from fastapi import FastAPI
from routers import productos, categorias

app = FastAPI(title="API de la Tienda")

# Conectamos los routers de cada recurso
app.include_router(productos.router)
app.include_router(categorias.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API de la Tienda funcionando. Visita /docs"}

from fastapi import FastAPI
from routers import auth, productos, categorias

app = FastAPI(title="API E-Commerce Segura")

app.include_router(auth.router)
app.include_router(productos.router)
app.include_router(categorias.router)