from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.learning_goal import LearningGoal
from app.models.learner_state import LearnerState

from app.services.dashboard_service import get_dashboard
from app.services.prompt_builder import build_ai_prompt
from app.services.gemini_service import ask_gemini

from fastapi import HTTPException


def ask_ai_mentor(
    db: Session,
    student_id: int,
    question: str
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

    prompt = build_ai_prompt(
        student,
        goal,
        state,
        dashboard,
        question
    )

    answer = ask_gemini(
        prompt
    )

    return answer