from pydantic import BaseModel
from typing  import Optional

# Define your signup model using pydantic BaseModel
class ProductModel(BaseModel):
    product_name: str
    weight: str
    price: int

# product update method
class ProductUpdate(BaseModel):
    product_id: int
    product_name: Optional[str] = None
    weight: Optional[str] = None
    price: Optional[int] = None