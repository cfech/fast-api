from typing import List
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schmas import UserBase, UserDisplay
from db import user_repository


router = APIRouter(prefix="/user", tags=["user"])

#create 
# The response from the db will be automatically mapped into the given response model
@router.post("/", response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return user_repository.create_user(db, user)

#read
@router.get("/", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return user_repository.get_all_users(db)

# read one element
@router.get("/{id}", response_model=UserDisplay)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return user_repository.get_user(db, id)

#update
@router.post("/{id}/update")
def updated_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return user_repository.update_user(db, id, request)

#delete
@router.delete("/{id}/delete")
def delete_user(id: int, db: Session = Depends(get_db)):
    return user_repository.delete_user(db, id)
