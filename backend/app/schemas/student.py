from pydantic import BaseModel
from sqlalchemy.orm import relationship

class StudentCreate(BaseModel):
    name: str
    goal: str
    learning_style: str