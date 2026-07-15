from pydantic import BaseModel
from datetime import datetime


class ConversationCreate(BaseModel):

    student_id: int

    question: str

    answer: str


class ConversationResponse(BaseModel):

    id: int

    student_id: int

    question: str

    answer: str

    created_at: datetime

    class Config:

        from_attributes = True