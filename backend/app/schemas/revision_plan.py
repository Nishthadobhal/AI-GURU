from pydantic import BaseModel


class RevisionPlanRequest(BaseModel):
    student_id: int
    days: int = 7


class RevisionPlanResponse(BaseModel):
    revision_plan: str