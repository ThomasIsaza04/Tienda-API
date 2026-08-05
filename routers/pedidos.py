from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
import seguridad

class ItemPedido(BaseModel):
    producto_id: int
    cantidad: int

class PedidoEntrada(BaseModel):
    items: List[ItemPedido]

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# Base de datos en memoria para pedidos
pedidos_db = [
    {
        "id": 1,
        "usuario": "ana",
        "items": [{"producto_id": 1, "cantidad": 2}],
        "estado": "completado"
    }
]

# --- ENDPOINTS PROTEGIDOS ---

# Listar pedidos (Un usuario ve los suyos, un Admin ve todos)
@router.get("", status_code=200)
def listar_pedidos(usuario: dict = Depends(seguridad.obtener_usuario_actual)):
    if usuario["rol"] == "admin":
        return pedidos_db
    
    # Filtrar solo los pedidos del cliente autenticado
    mis_pedidos = [p for p in pedidos_db if p["usuario"] == usuario["username"]]
    return mis_pedidos

# Consultar un pedido específico por ID
@router.get("/{pedido_id}", status_code=200)
def obtener_pedido(
    pedido_id: int,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    for pedido in pedidos_db:
        if pedido["id"] == pedido_id:
            # Validar que el pedido le pertenezca al usuario o que sea admin
            if pedido["usuario"] == usuario["username"] or usuario["rol"] == "admin":
                return pedido
            raise HTTPException(status_code=403, detail="No tienes permiso para ver este pedido")
            
    raise HTTPException(status_code=404, detail="Pedido no encontrado")

# Crear un nuevo pedido (Cualquier usuario autenticado)
@router.post("", status_code=201)
def crear_pedido(
    datos: PedidoEntrada,
    usuario: dict = Depends(seguridad.obtener_usuario_actual)
):
    nuevo_pedido = {
        "id": len(pedidos_db) + 1,
        "usuario": usuario["username"],
        "items": [item.model_dump() for item in datos.items],
        "estado": "pendiente"
    }
    pedidos_db.append(nuevo_pedido)
    return {"mensaje": "Pedido creado exitosamente", "pedido": nuevo_pedido}

# Eliminar/Cancelar pedido (Exclusivo Administradores)
@router.delete("/{pedido_id}", status_code=200)
def eliminar_pedido(
    pedido_id: int,
    admin: dict = Depends(seguridad.requerir_admin)
):
    for i, pedido in enumerate(pedidos_db):
        if pedido["id"] == pedido_id:
            pedidos_db.pop(i)
            return {"mensaje": f"Pedido {pedido_id} eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Pedido no encontrado")