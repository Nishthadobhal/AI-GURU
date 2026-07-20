from pydantic import BaseModel


class QuestionAnswer(BaseModel):
    question_id: int
    selected_answer: str


class QuizSubmission(BaseModel):
    student_id: int
    quiz_id: int
    time_taken_minutes: int
    answers: list[QuestionAnswer]


class QuizSubmissionResponse(BaseModel):
    score: float
    total_questions: int
    correct_answers: int