from sqlalchemy import Column, Boolean, String ,BigInteger


from database import Base


class User(Base):
    __tablename__ = "hostlr"

    Sl No=column(BigInteger,nullable=False)
    Name=Coulmn(String,nullable=False)
    Course=Column(String,nullable=False)
    Year_of_Study=Coulmn(BigInteger,nullable=False)
    Register Number=Column(BigInteger,primary_key=True)
    Dept=Column(String,nullable=False)
    Branch=Column(String,nullable=False)
    DOB=Coulmn(String,nullable=False)
    Blood_Group=Column(String,nullable=False)
    Nationality=Column(String,nullable=False)
    Community=Column(String,nullable=False)
    Religion=Column(String,nullable=False)
    Room_No=Column(BigInteger,nullable=False)
    Father_Name=Column(String,nullable=False)
    Mother_Name=Column(String,nullable=False)
    Gaurdian_Name=Column(String,nullable=True)
    Annual_Income_of_Parent/Gaurdian=Column(BigInteger,nullable=False)
    Mobile_no=Column(BigInteger,nullable=False)
    Residential_Address=Column(String,nullable=False)
    Communication_Address=Column(String,nullable=False)
    Parent_Mobie_No=Column(BigInteger,nullable=False)
    Mess_Requirements=Column(String,nullable=False)
