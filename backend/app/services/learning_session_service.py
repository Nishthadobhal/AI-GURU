from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.models.learning_session import LearningSession

from app.models.student import Student

from app.models.roadmap_topic import RoadmapTopic

from app.schemas.learning_event import LearningEventCreate

from app.services.learning_event_service import (
    create_learning_event
)


def create_learning_session(
    db: Session,
    data
):

    student = (
        db.query(Student)
        .filter(
            Student.id == data.student_id
        )
        .first()
    )


    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    topic = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.id == data.topic_id
        )
        .first()
    )


    if not topic:

        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )


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

            topic=topic.topic_name,

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