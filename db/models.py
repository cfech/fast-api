from sqlalchemy import Column, Integer, String
from db.database import Base


class DbUser(Base):
    # creates a db table
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)