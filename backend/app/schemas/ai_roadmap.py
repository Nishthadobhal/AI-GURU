from pydantic import BaseModel


class AIRoadmapRequest(BaseModel):

    student_id: int

    goal: str


class AIRoadmapResponse(BaseModel):

    roadmap: list[str]