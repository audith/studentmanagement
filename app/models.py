from sqlalchemy import Column,Integer,String
from .database import Base


class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    role=Column(String,default="student")
    department=Column(String,index=True)

    rank=Column(String)
    grade=Column(String)



