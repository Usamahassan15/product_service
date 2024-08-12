from sqlmodel import create_engine, Session, SQLModel, select
from .schema import ProductModel
from .model import product
from .schema import ProductUpdate
from .config import settings

# Create connecting of your  app with DB using create engine pkg
engine = create_engine(settings.database_url)

# Get Session
def get_session():
    SQLModel.metadata.create_all(engine)   # create all table defined in model.py 
    with Session(engine) as session:    # create session to send trasation in DB Table
        yield session

#---------------------------------------------------------------------------------------------------------

# store in db
def store(data: ProductModel, db: Session):
    new_product = product(
        product_name = data.product_name,
        weight = data.weight,
        price = data.price
    )

    db.add(new_product)        # save data in the session
    db.commit()                # save data in db 
    db.refresh(new_product)    # refresh new product with updated data in db 

    return new_product

#---------------------------------------------------------------------------------------------------------

def delete_product(id : int, db: Session):
    statement = select(product).where(product.id==id)
    product_info = db.exec(statement).first()
    db.delete(product_info)      
    db.commit()     # save changes in db 

    return f"Product with this {id} deleted successfully"

#--------------------------------------------------------------------------------------------------------

def get_product(id : int, db : Session):  #         user id  
    statement = select(product).where(product.id==id)
    product_info = db.exec(statement).first()
    
    return product_info

#----------------------------------------------------------------------------------------------------------

def update_product(product_input : ProductUpdate, db : Session):
    statement = select(product).where(product.id==product_input.product_id)
    product_info = db.exec(statement).first()

    if not product_info:
        return None
    
    if product_input.product_name is not None: 
        product_info.product_name = product_input.product_name

    if product_input.weight is not None:
        product_info.weight = product_input.weight

    if product_input.price is not None:
        product_info.price = product_input.price

    db.add(product_info)
    db.commit()         # commit means save data in db
    db.refresh(product_info)       

    return product_info

