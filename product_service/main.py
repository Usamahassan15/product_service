from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from .db import get_session
from .schema import ProductModel
from .db import store
from .db import delete_product
from .db import get_product
from .schema import ProductUpdate
from .db import update_product

app = FastAPI()

#---------------------------------------------------------------------------------------------------------

@app.post("/productinfo")
def add(data: ProductModel, db: Session = Depends(get_session)):   # custom type  :
    print(f"Data received in API:{data}")
    product = store(data,db)

    return product

#---------------------------------------------------------------------------------------------------------

@app.delete("/delete-product")
def remove(id : int, db: Session = Depends(get_session)):
    print(f"product id received{id}")
    message = delete_product(id,db)

    return message

#---------------------------------------------------------------------------------------------------------

@app.get("/get-product")
def read(id : int, db: Session = Depends(get_session)):
    print(f"product id received{id}")
    product = get_product(id,db)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")

    return product
    
#---------------------------------------------------------------------------------------------------------

@app.put("/put-product")
def update(product_input : ProductUpdate, db: Session = Depends(get_session)):
    print(f"Product input received{product_input}")
    product = update_product(product_input,db)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")

    return product