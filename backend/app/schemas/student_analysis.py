from pydantic import BaseModel


class StudentAnalysis(BaseModel):

    strongest_area: str

    weakest_area: str
    average_score: float
    overall_level: str