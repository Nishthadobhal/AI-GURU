from pydantic import BaseModel

class LearningEventCreate(BaseModel):
    student_id:int
    topic:str
    duration_minutes: int
    quiz_score: float | None = None
    revision: bool = False
    notes: str | None = None

class LearningEventResponse(BaseModel):
    id: int
    student_id: int
    topic: str
    duration_minutes: int
    quiz_score: int
    revision: bool
    notes: str
    revision: bool

    class Config:
        from_attributes = True