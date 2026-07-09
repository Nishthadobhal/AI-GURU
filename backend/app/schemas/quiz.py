from pydantic import BaseModel


class QuizCreate(BaseModel):

    topic_id: int

    title: str

    difficulty: str



class QuizResponse(BaseModel):

    id: int

    topic_id: int

    title: str

    difficulty: str


    class Config:
        from_attributes = True