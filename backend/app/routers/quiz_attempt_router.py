from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.quiz_attempt import (
    QuizAttemptCreate,
    QuizAttemptResponse
)

from app.services.quiz_attempt_service import (
    create_quiz_attempt
)


router = APIRouter(
    prefix="/quiz-attempts",
    tags=["Quiz Attempts"]
)


@router.post(
    "",
    response_model=QuizAttemptResponse
)
def add_quiz_attempt(
    attempt: QuizAttemptCreate,
    db: Session = Depends(get_db)
):

    return create_quiz_attempt(
        db,
        attempt
    )