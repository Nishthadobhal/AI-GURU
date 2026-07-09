from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.quiz import (
    QuizCreate,
    QuizResponse
)

from app.services.quiz_service import (
    create_quiz
)


router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"]
)


@router.post(
    "",
    response_model=QuizResponse
)
def add_quiz(
    quiz: QuizCreate,
    db: Session = Depends(get_db)
):

    return create_quiz(
        db,
        quiz
    )