from fastapi import APIRouter , Depends ,status,HTTPException
from sqlalchemy.orm import Session
from ..import schemas,models,database
from passlib.context import CryptContext
from ..repository import user


get_db =database.get_db
router = APIRouter(
    prefix="/user",
    tags=['Users'])

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated="auto")
@router.post('/',response_model=schemas.showUser)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.showUser)
def all(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)



