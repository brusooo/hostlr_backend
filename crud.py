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
        id=user.id,
        name=user.name,
        department=user.department,
        email=user.email,
        mobileNumber=user.mobileNumber,
        feePaid=user.feePaid,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jsonable_encoder(db_user)


