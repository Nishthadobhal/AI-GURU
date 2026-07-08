from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.learning_goal import (
    LearningGoalCreate,
    LearningGoalResponse
)

from app.services.learning_goal_service import (
    create_learning_goal
)

router = APIRouter(
    prefix="/learning-goals",
    tags=["Learning Goals"]
)


@router.post(
    "",
    response_model=LearningGoalResponse
)
def add_learning_goal(
    goal: LearningGoalCreate,
    db: Session = Depends(get_db)
):

    return create_learning_goal(
        db,
        goal
    )