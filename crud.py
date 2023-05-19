from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import models, schemas
from sqlalchemy import select,update,delete
from datetime import date , time

def get_user_by_id(db: Session, user_id: int):
    stmt = select(models.permission).where(models.permission.id == user_id)
    return jsonable_encoder(db.scalars(stmt).first())


# def get_user_by_dept(db: Session, dept: str) -> list[object]:
#     stmt = select(models.permission).where(models.User.department == dept)
#     return jsonable_encoder(db.scalars(stmt).all())


def get_all_users(db: Session):
    return jsonable_encoder(db.scalars(select(models.permission)).all())


def create_user(db: Session, permission: schemas.permission):
    db_user = models.permission(
        id=permission.id,
        from_=permission.from_,
        to_=permission.to_,
        reason_=permission.reason_,
        informed_parent_on=permission.informed_parent_on,
    
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jsonable_encoder(db_user)

def remove_book(db: Session, id: int):
    user = get_user_by_id(db=db, id=id)
    db.delete(user)
    db.commit()



def update_user(db: Session, id: int, from_: date,to_:date, reason_: str, informed_parent_on: time):
    user = get_user_by_id(db=db, user_id=id)

    user[id] = id
    user[from_] = from_
    user[to_] = to_
    user[reason_] = reason_
    user[informed_parent_on] = informed_parent_on
    


    stmt = (update(models.permission).where(models.permission.id == id).values(from_ =from_,to_=to_,reason_=reason_,informed_parent_on = informed_parent_on))
    db.execute(stmt)
    db.commit()
    
    return "succesfully updated"


def delete_user(db: Session, id: int):
    user = get_user_by_id(db=db, user_id=id)

    user[id] = id
    
    stmt = (delete(models.permission).where(models.permission.id == id))
    db.execute(stmt)
    db.commit()
    
    return "succesfully deleted"



