from pydantic import BaseModel


class LearningSessionCreate(BaseModel):

    student_id: int

    topic_id: int

    duration_minutes: int

    completed: bool



class LearningSessionResponse(BaseModel):

    id: int

    student_id: int

    topic_id: int

    duration_minutes: int

    completed: bool


    class Config:
        from_attributes = True