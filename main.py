from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine
from schemas import RequestUser, permission


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def show_opening_page():
    return {"message": "continue"}


@app.get("/users/all")
def get_all_users(db: Session = Depends(get_db)):
    db_user = crud.get_all_users(db)
    result_dict = {}
    for idx, user in enumerate(db_user):
        result_dict[f"{idx}"] = jsonable_encoder(user)
    return jsonable_encoder(result_dict)


@app.get("/users/id/{user_id}", response_model=schemas.permission)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user)

@app.get("/users/dept/{dept}", response_model=object)
def read_user_by_dept(dept: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_dept(db, dept=dept)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user)


@app.post("/users/create", response_model=schemas.permission)
def create_user(permission: schemas.permission, db: Session = Depends(get_db)):
    return crud.create_user(db, permission)

# @app.post('/api/submit')
# def submit_form(data: FormData):
#     # Create a new session
#     session = SessionLocal()

#     # Create a new instance of the SubmittedData model
#     submitted_data = SubmittedData(name=data.name, email=data.email)

#     # Add the new data to the session
#     session.add(submitted_data)
#     session.commit()

#     return {'message': 'Submitted successfully'}




# @app.patch("/heroes/{hero_id}")
# def update_user(id: int, hero: HeroUpdate):
#     with Session(engine) as session:
#         db_hero = session.get(Hero, hero_id)
#         if not db_hero:
#             raise HTTPException(status_code=404, detail="Hero not found")
#         hero_data = hero.dict(exclude_unset=True)
#         for key, value in hero_data.items():
#             setattr(db_hero, key, value)
#         session.add(db_hero)
#         session.commit()
#         session.refresh(db_hero)
#         return db_hero

@app.post("/updateuser/{id_}")
def update_user(id_:int,request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(db, id=id_,
                             from_=request.from_,to_=request.to_, reason_=request.reason_,  informed_parent_on= request.informed_parent_on)
    return _user

@app.patch("/deleteuser/{id}")
def delete_user(request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.delete_user(db, id=request.id)
    return _user

# @router.get("/")
# async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     _books = crud.get_book(db, skip, limit)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=_books)


# @router.delete("/delete")
# async def delete_book(request: RequestBook,  db: Session = Depends(get_db)):
#     crud.remove_book(db, book_id=request.parameter.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
