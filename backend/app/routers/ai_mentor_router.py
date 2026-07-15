from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.ai_mentor import (
    AIMentorRequest,
    AIMentorResponse
)

from app.services.ai_mentor_service import (
    ask_ai_mentor
)

router = APIRouter()


@router.post(
    "/ai-mentor",
    response_model=AIMentorResponse
)
def ai_mentor(
    data: AIMentorRequest,
    db: Session = Depends(get_db)
):

    answer = ask_ai_mentor(
        db,
        data.student_id,
        data.question
    )

    return AIMentorResponse(
        answer=answer
    )