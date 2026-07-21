from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.quiz_attempt_history import (
    QuizAttemptHistory,
)

from app.services.quiz_attempt_history_service import (
    get_quiz_attempt_history,
)

router = APIRouter(
    tags=["Quiz Attempt History"]
)


@router.get(
    "/students/{student_id}/quiz-attempts",
    response_model=List[QuizAttemptHistory]
)
def get_student_quiz_attempts(
    student_id: int,
    db: Session = Depends(get_db)
):

    return get_quiz_attempt_history(
        db=db,
        student_id=student_id
    )