from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Simulating a dictionary as fake database
db = {}

class Item(BaseModel):
    name: str
    address: str


def generate_id():
    return max(db.keys(),default=0)+1

@app.get("/")
def load_homepage():
    return {"message": "Hello World!!"}

@app.post("/items/",response_model=Item)
def create_item(new_item: Item):
    id = generate_id()
    db[id]=new_item
    return new_item


@app.get("/items/",response_model=List[Item])
def fetch_all():
    return list(db.values())

 

