from pydantic import BaseModel

class LearningEventCreate(BaseModel):
    student_id:int
    topic:str
    duration_minutes: int
    quiz_score: float | None = None
    revision: bool = False
    notes: str | None = None