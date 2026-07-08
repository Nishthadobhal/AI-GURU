from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.learning_session import (
    LearningSessionCreate,
    LearningSessionResponse
)

from app.services.learning_session_service import (
    create_learning_session
)


router = APIRouter(
    prefix="/learning-sessions",
    tags=["Learning Sessions"]
)


@router.post(
    "",
    response_model=LearningSessionResponse
)
def add_learning_session(
    session: LearningSessionCreate,
    db: Session = Depends(get_db)
):

    return create_learning_session(
        db,
        session
    )