from fastapi import Depends, FastAPI,status,HTTPException,Response
from starlette.status import HTTP_201_CREATED
from .import schemas
from .import models
from .database import engine,Sessionlocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def  get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/product",status_code=status.HTTP_201_CREATED)
def add(request:schemas.Product, db: Session = Depends(get_db)):
    new_product=models.Product(
        name=request.name,
        description=request.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)


    return new_product.id

@app.get(f"/product/{id}")
def getproduct(id,response:Response,db: Session = Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id==id).first()
    if not product:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail="product is not found"
                            )
        #response.status_code=status.HTTP_404_NOT_FOUND
    return product

@app.delete(f"/product/{id}")
def delete(id,db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id==id).delete(synchronize_session=False)
    db.commit()

@app.put(f"/product/{id}")
def update(id,request:schemas.Product,db:Session = Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id==id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {f"Product updated successfully for {id}"}


@app.post("/seller",status_code=HTTP_201_CREATED)
def createseller(request:schemas.Seller,db: Session = Depends(get_db)):
    new_seller=models.Seller(
        name=request.name,
        email=request.email,
        password=request.password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)


    return new_seller.id
   




