from pydantic import BaseModel
from typing import List

class StudentReport(BaseModel):
    features: dict
    topic_analysis: dict
    consistency_score: float
    state: dict
    readiness: float
    recommendation: List[str]