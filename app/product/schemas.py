from pydantic import BaseModel

class Product(BaseModel):
    name:str
    description:str

class Seller(BaseModel):
    name:str
    email:str
    password:str