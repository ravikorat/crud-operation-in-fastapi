from sqlalchemy.orm import Session
from .. import schemas,models
from fastapi import HTTPException,status
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated="auto")
def create(request:schemas.User,db:Session):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name = request.name,email = request.email,password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"User with the id {id} is not available")
    return users