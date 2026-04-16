from sqlalchemy.orm import Session
from .import models,schemas

def create_student(db:Session,student:schemas.StudentCreate):
    db_student=models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db:Session):
    return db.query(models.Student).all()


def update_student(db:Session,student_id:int,data:schemas.StudentUpdate):
    student=db.query(models.Student).filter(models.Student.id==student_id).first()
    if not student:
        return {"massge":"student not exists in database"}
    for key,value in data.dict(exclude_unset=True).items():
        setattr(student,key,value)

    db.commit()
    db.refresh(student)
    return student


def delete_student(db:Session,student_id:int):
    student=db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return {"massage":"student nor exists"}
    db.delete(student)
    db.commit()
    return student
    


