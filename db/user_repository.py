
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schmas import UserBase

# Will have 3 data types
# UserBase - model that comes from the user
# DbUser - information that is in the table
#  - information returned for a user 

def create_user(db: Session, request: UserBase):
    # Create the user
    new_user = DbUser(username = request.username, email = request.email, password = Hash.bcrypt(request.password))

    # Start the transaction
    db.add(new_user)

    # Commit the transaction
    db.commit()

    # Refreshes the user object will get any db updated fields (ie: generated ID)
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    # return all the entries in the db table
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    print("searching for id ====> ", id)
    return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(db: Session, id : int, updated_user: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: updated_user.username,
        DbUser.email: updated_user.email,
        DbUser.password: Hash.bcrypt(updated_user.password)
    })

    db.commit()
    return "Ok"

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "OK"