from sqlalchemy.orm import Session

from app.models.learning_session import LearningSession


def create_learning_session(
    db: Session,
    data
):

    session = LearningSession(
        student_id=data.student_id,
        topic_id=data.topic_id,
        duration_minutes=data.duration_minutes,
        completed=data.completed
    )


    db.add(session)

    db.commit()

    db.refresh(session)


    return session