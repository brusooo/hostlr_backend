from pydantic import BaseModel

class User(BaseModel):
    Sl_No :int
    Name : str
    Course:str
    Year_of_Study:int
    Register_Number:int
    Dept:str
    Branch:str
    DOB:int
    Blood_Group:str
    Nationality:str
    Community:str
    Religion:str
    Father_Name:str
    Mother_Name:str
    Gaurdian_Name:str
    Annual_Income_of_Parent:int
    Mobile_no:int
    Residential_Address:str
    Communication_Address:str
    Parent_Mobile_No:int
    Room_No:int
    Mess_Requirements:str
   
