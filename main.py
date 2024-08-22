from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

productos = []

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: int

@app.post("/products/", response_model=Producto)
def crear_producto(producto: Producto):
    for p in producto:
        if p.id == producto.id:
            raise HTTPException(status_code=400, detail="No existe producto con esa ID -_:c_-")
        
        productos.append(producto)
        return producto

@app.get("/products/", response_model=list[Producto])
def mostrar_producto():
    return productos 
    

@app.get("/products/{producto_id}")
def mostrar_productoId(producto_id: int):
    for product in productos:
        if product.id == producto_id:
            return product
    
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.put("/products/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, update_product: Producto):
    for index, product in enumerate(productos):
        if product.id == producto_id:
            productos[index] = update_product
            return update_product
    
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/products/{producto_id}")
def eliminar_producto(producto_id: int):
    for index, product in enumerate(productos):
        if product.id == producto_id:
            del productos[index]
            return {"message": "Producti eliminado Correctamente!!"}
        
    raise HTTPException(status_code=404, detail="Producto no encontrado")

