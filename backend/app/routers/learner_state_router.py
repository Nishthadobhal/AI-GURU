from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.learner_state import LearnerStateResponse
from app.services.learner_state_service import (
    get_learner_state,
)

router = APIRouter()


@router.get(
    "/students/{student_id}/learner-state",
    response_model=LearnerStateResponse,
)
def fetch_learner_state(
    student_id: int,
    db: Session = Depends(get_db),
):
    state = get_learner_state(
        db,
        student_id,
    )

    if state is None:
        raise HTTPException(
            status_code=404,
            detail="Learner State not found."
        )

    return state