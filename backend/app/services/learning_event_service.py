from sqlalchemy.orm import Session

from app.models.learning_event import LearningEvent
from app.schemas.learning_event import LearningEventCreate


def create_learning_event(
    db: Session,
    learning_event: LearningEventCreate
):
    db_learning_event = LearningEvent(
        student_id=learning_event.student_id,
        topic=learning_event.topic,
        duration_minutes=learning_event.duration_minutes,
        quiz_score=learning_event.quiz_score,
        revision=learning_event.revision,
        notes=learning_event.notes
    )

    db.add(db_learning_event)
    db.commit()
    db.refresh(db_learning_event)

    return db_learning_event

def get_learning_events_by_student(
    db: Session,
    student_id: int
):
    return (
        db.query(LearningEvent)
        .filter(LearningEvent.student_id == student_id)
        .all()
    )