from pydantic import BaseModel, ConfigDict

# This will be our POJO
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

    # config updated to this syntax in pydantic v2
    model_config = ConfigDict(from_attributes=True)
    # # This is a config for this class
    # class Config():
    #     # This setting allows the db to automatically convert the model DBUser into this type
    #     from_attributes = True