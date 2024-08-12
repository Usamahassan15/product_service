from sqlmodel import SQLModel, Field
from typing import Optional 

class product(SQLModel,table=True):
    id: Optional [int] =  Field(primary_key=True,default=None)
    product_name: str
    weight: str
    price: int