from fastapi import FastAPI
    # lib           # class
from models import Product
app = FastAPI()

# all REST API Method functions are by default async here
@app.get("/")
def greet():
    return "Welcome Buddy"

# ! This was withou pydantic
# prod_list = [
#     Product(1,'Macbook M1', 'M1 Series Macbook Air', 50000),
#     Product(1,'Macbook M2', 'M2 Series Macbook Air', 80000),
# ]

# ! with pydantic
prod_list = [
    Product(id=1,name='Macbook M1',description='M1 Series Macbook Air', price=50000),
    Product(id=2,name='Macbook M2',description='M2 Series Macbook Air', price=80000),
    Product(id=3,name='Macbook M3',description='M3 Series Macbook Air', price=80000),
    Product(id=4,name='Macbook M4',description='M4 Series Macbook Air', price=80000),
]

@app.get('/products')
def get_all_products():
    return prod_list

# @app.get('/product/{id}')
# def get_a_product(id:int):
#     return prod_list[id-1]  # * index adjustment

# ! The above method will fail when the ids are not in sequential order and thus we need a more robust implementation here where we actually search the product from the list

@app.get('/product/{id}')
def get_a_product(id:int):
    for product in prod_list:
        if product.id == id:
            return product
        
    return 'Product Not Found'


@app.post('/product')
def add_a_product(product:Product):
    prod_list.append(product)
    return product

@app.put('/product')
def update_product(id:int, product:Product):
    for i in range(len(prod_list)):
        if id == prod_list[i].id:
            prod_list[i] = product
            return f'Product Update Successfully {product}'
    
    return 'No Such Product Found'


@app.delete('/product')
def delete_product(id:int):
    for i in range(len(prod_list)):
        if prod_list[i].id == id:
            del prod_list[i]
            return 'Product Deleted'
    
    return 'No such product found'

# * It is better to use range function while iterating rather than direct iterating like : for i in prod_list