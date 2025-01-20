from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schmas import UserBase, UserDisplay
from db import db_user


router = APIRouter(prefix="/user", tags=["user"])

#create 
# The response from the db will be automatically mapped into the given response model
@router.post("/", response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, user)

#read

#update

#delete

