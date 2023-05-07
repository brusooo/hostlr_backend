from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import models, schemas
from sqlalchemy import select


def get_user_by_id(db: Session, user_id: int):
    stmt = select(models.User).where(models.User.id == user_id)
    return jsonable_encoder(db.scalars(stmt).first())


def get_user_by_dept(db: Session, dept: str) -> list[object]:
    stmt = select(models.User).where(models.User.department == dept)
    return jsonable_encoder(db.scalars(stmt).all())


def get_all_users(db: Session):
    return jsonable_encoder(db.scalars(select(models.User)).all())


def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        
        Sl_No=user.Sl_No,
        Name=user.Name,
        Course=user.Course,
        Year_of_Study=user.Year_of_Study,
        Register_Number=user.Register_Number,
        Dept=user.Dept,
        Branch=user.Branch,
        DOB=user.DOB,
        Blood_Group=user.Blood_Group,
        Nationality=user.Nationality,
        Community=user.Community,
        Religion=user.Religion,
        Father_Name=user.Father_Name,
        Mother_Name=user.Mother_Name,
        Gaurdian_Name=user.Gaurdian_Name,
        Annual_Income_of_Parent=user.Annual_Income_of_Parent,
        Mobile_no=user.Mobile_no,
        Residential_Address=user.Residential_Address,
        Communication_Address=user.Communication_Address,
        Parent_Mobile_No=user.Parent_Mobile_No,
        Room_No=user.Room_No,
        Mess_Requirements=user.Mess_Requirements
   
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jsonable_encoder(db_user)


