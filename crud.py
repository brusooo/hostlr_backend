from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import models, schemas
from sqlalchemy import select,update,delete
from datetime import date , time




def get_user_by_id(db: Session, user_id: int):
    stmt = select(models.permission).where(models.permission.id == user_id)
    return jsonable_encoder(db.scalars(stmt).first())



def get_all_accepted(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by == 'notaccepted')
    return jsonable_encoder(db.scalars(stmt).all())

def get_all_acceptedhod1(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by == 'hodaccepted')
    return jsonable_encoder(db.scalars(stmt).all())


def get_all_acceptedhod(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by.in_(["hodaccepted" , "wadernaccepted" , "waderndenied"]))
    return jsonable_encoder(db.scalars(stmt).all())

def get_all_acceptedwadern(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by == 'wadernaccepted')
    return jsonable_encoder(db.scalars(stmt).all())

def get_all_deniedwadern(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by == 'waderndenied')
    return jsonable_encoder(db.scalars(stmt).all())


def get_all_deniedhod(db: Session) :
    stmt = select(models.permission).where(models.permission.accepted_by == 'hoddenied')
    return jsonable_encoder(db.scalars(stmt).all())


def get_all_users(db: Session):
    return jsonable_encoder(db.scalars(select(models.permission)).all())

def get_all_permission(db: Session, stuid_: int) :
    stmt = select(models.permission).where(models.permission.stuid_ == stuid_ )
    return jsonable_encoder(db.scalars(stmt).all())

# def get_all_accepted(db: Session):
#     items = session.query(models.permission).filter(models.permission.accepted_by == 'notaccepted').all()
#     return jsonable_encoder(db.scalars(select(models.permission)).all())


def create_user(db: Session, permission: schemas.permission):
    db_user = models.permission(
        id=permission.id,
        stuid_ = permission.stuid_,
        from_=permission.from_,
        to_=permission.to_,
        accepted_by = permission.accepted_by,
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



def update_user(db: Session, id: int,stuid_ : int, from_: date,to_:date, reason_: str,accepted_by:str, informed_parent_on: time):
    user = get_user_by_id(db=db, user_id=id)

    user[id] = id
    user[stuid_] = stuid_
    user[from_] = from_
    user[to_] = to_
    user[accepted_by] = accepted_by
    user[reason_] = reason_
    user[informed_parent_on] = informed_parent_on
    


    stmt = (update(models.permission).where(models.permission.id == id).values(stuid_ = stuid_,from_ =from_,to_=to_,reason_=reason_,accepted_by = accepted_by,informed_parent_on = informed_parent_on))
    db.execute(stmt)
    db.commit()
    
    return "succesfully updted"


def delete_user(db: Session, id: int):
    user = get_user_by_id(db=db, user_id=id)

    user[id] = id
    
    stmt = (delete(models.permission).where(models.permission.id == id))
    db.execute(stmt)
    db.commit()
    
    return "succesfully deleted"




