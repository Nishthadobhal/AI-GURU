from pydantic import BaseModel


class QuizAttemptCreate(BaseModel):

    student_id: int

    quiz_id: int

    score: float

    time_taken_minutes: int



class QuizAttemptResponse(BaseModel):

    id: int

    student_id: int

    quiz_id: int

    score: float

    time_taken_minutes: int


    class Config:
        from_attributes = True