from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.analytics import StudentReport
from app.services.learning_event_service import (
    get_learning_events_by_student,
)
from app.services.analytics_service import (
    generate_student_report,
)

router = APIRouter()


@router.get(
    "/students/{student_id}/report",
    response_model=StudentReport,
)
def get_student_report(
    student_id: int,
    db: Session = Depends(get_db),
):
    events = get_learning_events_by_student(db, student_id)

    if not events:
        raise HTTPException(
            status_code=404,
            detail="No learning events found."
        )

    return generate_student_report(events)