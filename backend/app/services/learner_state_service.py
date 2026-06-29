from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState


def get_learner_state(
    db: Session,
    student_id: int
):
    return (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )