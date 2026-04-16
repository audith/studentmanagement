from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session


from . import models,schemas,crud
from . database import engine,SessionLocal,Base
from .deps import get_admin


Base.metadata.create_all(bind=engine)

app=FastAPI(title="Student management system")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students")
def create_students(students:schemas.StudentCreate,db:Session=Depends(get_db),admin:bool=Depends(get_admin)):
    return crud.create_student(db,students)


@app.get("/students",response_model=list[schemas.StudentOut])
def read_students(db:Session=Depends(get_db)):
    return crud.get_students(db)


@app.put("/students/{student_id}")
def update_student(student_id:int,data:schemas.StudentUpdate,db:Session=Depends(get_db),admin:bool=Depends(get_admin)):
    return crud.update_student(db,student_id,data)


@app.delete("/student/{student_id}")
def student_delete(student_id:int,db:Session=Depends(get_db),admin:bool=Depends(get_admin)):
    return crud.delete_student(db,student_id)



