from pydantic import BaseModel


class StudentReport(BaseModel):
    features: dict
    topic_analysis: dict
    consistency_score: float
    state: dict
    readiness: float
    recommendation: str