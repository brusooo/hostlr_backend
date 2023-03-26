from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    department : str
    email : str
    mobileNumber : int
    feePaid : bool
