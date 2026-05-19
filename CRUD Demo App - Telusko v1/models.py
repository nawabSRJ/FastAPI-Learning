
from pydantic import BaseModel
# ! without pydantic
# class Product:
#     id:int
#     name:str
#     description:str
#     price:float

#     def __init__(self, id:int, name:str, desc:str, price:float):
#         self.id = id
#         self.name = name
#         self.description = desc
#         self.price = price
        

# ! With pydantic 
# * Here you don't need to make constructor, that is automatically taken care of but when initializing then you need to pass the identifier name as well or class attribute name unlike Without pydantic method which works like positional arguments

class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float


        