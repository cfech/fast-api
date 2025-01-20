from pydantic import BaseModel

# This will be our POJO
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    # This is a config for this class
    class Config():
        # This setting allows the db to automatically convert the model DBUser into this type
        orm_mode = True