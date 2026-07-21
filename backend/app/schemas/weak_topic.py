from pydantic import BaseModel


class WeakTopic(BaseModel):
    topic: str
    average_score: float


class WeakTopicResponse(BaseModel):
    student_id: int
    weak_topics: list[WeakTopic]