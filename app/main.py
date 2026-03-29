from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import List,Set


class Profile(BaseModel):
    name: str
    email: str
    age:float
    
class Product(BaseModel):
    name: str
    price: float = Field(description="The price of the product")
    age:float
    tags:Set[str] = []


app = FastAPI()


@app.get("/")
def index() -> str:
    return "Hello World!"

@app.get("/movies")
def movies():
    return {
        'Title':'New Movie',
        'Year': '2009'
    }


@app.get("/movies/{id}")
def movies(id:int):
    return {
        'Title':'New Movie',
        'Year': '2009',
        'id':{id}
    }

@app.get("/products/")
def products(id:int=1,price:float=0.0):
    return {
        f'The price and product for given {id} is {price}'
    }

@app.post("/adduser")
def adduser(profile:Profile):
    return profile


@app.post("/addproduct/{product_id}")
def addproduct(product:Product,product_id):
    return product
