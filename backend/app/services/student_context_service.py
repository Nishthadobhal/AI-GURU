from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.learning_goal import LearningGoal
from app.models.learner_state import LearnerState

from app.services.dashboard_service import get_dashboard
from app.services.conversation_service import (
    get_recent_conversations
)

from fastapi import HTTPException


def get_student_context(
    db: Session,
    student_id: int
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    goal = (
        db.query(LearningGoal)
        .filter(LearningGoal.student_id == student_id)
        .first()
    )

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Learning goal not found"
        )

    state = (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )

    if not state:
        raise HTTPException(
            status_code=404,
            detail="Learner state not found"
        )

    dashboard = get_dashboard(
        db,
        student_id
    )

    conversations = get_recent_conversations(
        db,
        student_id
    )

    return {
        "student": student,
        "goal": goal,
        "state": state,
        "dashboard": dashboard,
        "conversations": conversations
    }