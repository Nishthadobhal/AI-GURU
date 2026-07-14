from pydantic import BaseModel


class StudentAnalysis(BaseModel):

    strongest_area: str

    weakest_area: str

    overall_level: str