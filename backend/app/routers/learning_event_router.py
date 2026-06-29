from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.learning_event import LearningEventCreate
from app.services.learning_event_service import (
    create_learning_event,
    get_learning_events_by_student
)

router = APIRouter()


@router.post("/learning-events")
def add_learning_event(
    learning_event: LearningEventCreate,
    db: Session = Depends(get_db)
):
    return create_learning_event(db, learning_event)



@router.get("/student/{student_id}/learning-events")
def get_learning_events(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_learning_events_by_student(
        db,
        student_id
    )