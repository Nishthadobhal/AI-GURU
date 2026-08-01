from pydantic import BaseModel
from sqlalchemy.orm import relationship

class StudentCreate(BaseModel):
    name: str
    goal: str
    learning_style: str


class StudentLogin(BaseModel):
    name: str

class StudentResponse(BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True