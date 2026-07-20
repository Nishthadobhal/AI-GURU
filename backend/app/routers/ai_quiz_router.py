from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.quiz_generation import (
    QuizGenerationRequest
)

from app.services.ai_quiz_service import (
    generate_quiz_from_ai
)

router = APIRouter(
    prefix="/ai",
    tags=["AI Quiz"]
)


@router.post("/generate-quiz")
def generate_quiz(
    data: QuizGenerationRequest,
    db: Session = Depends(get_db)
):

    result = generate_quiz_from_ai(
        db=db,
        topic_id=data.topic_id,
        difficulty=data.difficulty,
        number_of_questions=data.number_of_questions
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )

    return result