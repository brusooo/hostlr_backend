from pydantic import BaseModel
from pydantic import  Field
from datetime import date,time

class permission(BaseModel):
    id : int
    from_ : date
    to_ : date
    reason_ : str
    informed_parent_on : time
    

class RequestUser(permission):
    pass
# class FormData(BaseModel):
#     name: str
#     from_ :date
#     to: date
#     reason:str
#     ifprmed_Parent_On:str
