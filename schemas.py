from pydantic import BaseModel
from pydantic import  Field
from datetime import date,time

class perm(BaseModel):
    id : int
  
    reason_ : str

   

class permission(BaseModel):
    id : int
    stuid_ : int
    from_ : date
    to_ : date
    accepted_by :str
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
