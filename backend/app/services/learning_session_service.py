from sqlalchemy.orm import Session

from app.models.learning_session import LearningSession

from app.schemas.learning_event import LearningEventCreate

from app.services.learning_event_service import (
    create_learning_event
)


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


    if data.completed:

        event = LearningEventCreate(

            student_id=data.student_id,

            topic="Roadmap Topic",

            duration_minutes=data.duration_minutes,

            quiz_score=0,

            revision=False,

            notes="Generated from learning session"

        )


        create_learning_event(
            db,
            event
        )


    return session