from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.question import (
    QuestionCreate,
    QuestionResponse
)

from app.services.question_service import (
    create_question
)
from typing import List

from app.schemas.question import (
    QuestionForQuiz,
)

from app.services.question_service import (
    get_questions_by_quiz,
)
router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post(
    "",
    response_model=QuestionResponse
)
def add_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):

    return create_question(
        db,
        question
    )

@router.get(
    "/quizzes/{quiz_id}/questions",
    response_model=List[QuestionForQuiz]
)
def get_quiz_questions(
    quiz_id: int,
    db: Session = Depends(get_db)
):

    return get_questions_by_quiz(
        db,
        quiz_id
    )