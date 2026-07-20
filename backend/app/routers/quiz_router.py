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
from app.services.quiz_service import (
    create_quiz,
    get_quizzes_by_topic
)

from typing import List

from app.schemas.quiz import QuizResponse
from app.schemas.quiz_submission import (
    QuizSubmission,
    QuizSubmissionResponse,
)

from app.services.quiz_service import (
    submit_quiz,
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

@router.get(
    "/topic/{topic_id}",
    response_model=List[QuizResponse]
)
def get_topic_quizzes(
    topic_id: int,
    db: Session = Depends(get_db)
):

    return get_quizzes_by_topic(
        db,
        topic_id
    )

@router.post(
    "/quizzes/submit",
    response_model=QuizSubmissionResponse
)
def submit_student_quiz(
    data: QuizSubmission,
    db: Session = Depends(get_db)
):

    result = submit_quiz(db, data)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found or has no questions."
        )

    return result