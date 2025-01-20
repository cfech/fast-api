# Configuring SQL Alchemy ORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the db connection string 
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Will be used to generate models
Base = declarative_base()


# this is a generator function to produce a db connection
def get_db():
    db = SessionLocal()
    try:
        # Gives you a value, pauses the function, and remembers its state so it can continue to take further action later
        yield db
    finally:
        # In this case eventually we will hit this finally and the db connection will close
        db.close()
