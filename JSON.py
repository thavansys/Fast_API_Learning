from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/json")
def receive_json(item: Item):
    return {
        "type": "JSON",
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }