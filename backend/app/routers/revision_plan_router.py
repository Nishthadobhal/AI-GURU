from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.revision_plan import (
    RevisionPlanRequest,
    RevisionPlanResponse,
)

from app.services.revision_plan_service import (
    generate_revision_plan,
)

router = APIRouter(
    prefix="/revision-plan",
    tags=["Revision Planner"]
)


@router.post(
    "",
    response_model=RevisionPlanResponse
)
def create_revision_plan(
    request: RevisionPlanRequest,
    db: Session = Depends(get_db)
):

    return generate_revision_plan(
        db=db,
        student_id=request.student_id,
        days=request.days
    )