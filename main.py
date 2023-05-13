from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine


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

@app.get("/testget")
def show_opening_page():
    return {"id": "1","name":"Rathish","Dept":"CSE"}

@app.get("/users/all")
def get_all_users(db: Session = Depends(get_db)):
    db_user = crud.get_all_users(db)
    result_dict = {}
    for idx, user in enumerate(db_user):
        result_dict[f"{idx}"] = jsonable_encoder(user)
    return jsonable_encoder(result_dict)


@app.get("/users/id/{user_id}", response_model=schemas.User)
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


@app.post("/users/create", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post('/api/submit')
def submit_form(data: FormData):
    # Create a new session
    session = SessionLocal()

    # Create a new instance of the SubmittedData model
    submitted_data = SubmittedData(name=data.name, email=data.email)

    # Add the new data to the session
    session.add(submitted_data)
    session.commit()

    return {'message': 'Submitted successfully'}



@app.patch("/updateuser/{id}")
def update_user(request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(db, id=request.id,
                             name=request.name, email=request.email, mobilenumber = request.mobilenumber, feepaid=request.feepaid)
    return _user

@app.patch("/deleteuser/{id}")
def delete_user(request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.delete_user(db, id=request.id)
    return _user
