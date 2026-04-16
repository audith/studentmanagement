from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    name:str
    role:str="stident"
    department:Optional[str]=None
    rank:str
    grade:str


class StudentUpdate(BaseModel):
    name:Optional[str]=None
    role:Optional[str]=None
    department:Optional[str]=None
    rank:Optional[str]=None
    grade:Optional[str]=None


class StudentOut(BaseModel):
    id:int
    name:str
    role:str
    department:Optional[str]
    rank:str
    grade:str

    class Config:
        orm_mode=True