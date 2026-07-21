from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.weak_topic import (
    WeakTopicResponse,
)

from app.services.weak_topic_service import (
    get_weak_topics,
)

router = APIRouter(
    tags=["Weak Topics"]
)


@router.get(
    "/students/{student_id}/weak-topics",
    response_model=WeakTopicResponse
)
def get_student_weak_topics(
    student_id: int,
    db: Session = Depends(get_db)
):

    return get_weak_topics(
        db=db,
        student_id=student_id
    )