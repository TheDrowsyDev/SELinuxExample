from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int

items = [Item(name="Pencils", quantity=117),
         Item(name="Desk Chairs", quantity=8),
         Item(name="Printer Ink Cartridges", quantity=25)]

app = FastAPI()

@app.post("/items/")
def create_item(item: Item) -> Item:
    return item

@app.get("/items/")
def list_items() -> list[Item]:
    return items