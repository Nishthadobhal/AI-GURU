from pydantic import BaseModel


class QuizGenerationRequest(BaseModel):

    topic_id: int

    difficulty: str = "Easy"

    number_of_questions: int = 5