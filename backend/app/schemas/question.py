from pydantic import BaseModel


class QuestionCreate(BaseModel):

    quiz_id: int

    question_text: str

    option_a: str

    option_b: str

    option_c: str

    option_d: str

    correct_answer: str


class QuestionResponse(BaseModel):

    id: int

    quiz_id: int

    question_text: str

    option_a: str

    option_b: str

    option_c: str

    option_d: str

    correct_answer: str

    class Config:
        from_attributes = True