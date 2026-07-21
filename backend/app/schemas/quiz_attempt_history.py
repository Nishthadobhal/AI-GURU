from datetime import datetime

from pydantic import BaseModel


class QuizAttemptHistory(BaseModel):
    quiz_id: int
    quiz_title: str
    score: int
    attempted_at: datetime

    class Config:
        from_attributes = True