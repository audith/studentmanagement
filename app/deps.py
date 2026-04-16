from fastapi import Header,HTTPException


def get_admin(x_role:str = Header(default="student")):
    if x_role is not "admin":
        raise HTTPException(status_code=403,detail="only admin can accesde")
    return True