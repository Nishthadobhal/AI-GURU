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