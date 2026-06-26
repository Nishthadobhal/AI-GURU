from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    goal: str
    learning_style: str