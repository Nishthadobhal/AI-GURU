from pydantic import BaseModel


class StudentReport(BaseModel):
    features: dict
    state: dict
    recommendation: str