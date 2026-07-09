from sqlalchemy.orm import Session

from app.models.quiz_attempt import QuizAttempt

from app.models.quiz import Quiz

from app.models.roadmap_topic import RoadmapTopic

from app.schemas.learning_event import LearningEventCreate

from app.services.learning_event_service import (
    create_learning_event
)


def create_quiz_attempt(
    db: Session,
    data
):

    attempt = QuizAttempt(
        student_id=data.student_id,
        quiz_id=data.quiz_id,
        score=data.score,
        time_taken_minutes=data.time_taken_minutes
    )


    db.add(attempt)

    db.commit()

    db.refresh(attempt)


    quiz = (
        db.query(Quiz)
        .filter(
            Quiz.id == data.quiz_id
        )
        .first()
    )


    topic = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.id == quiz.topic_id
        )
        .first()
    )


    event = LearningEventCreate(

        student_id=data.student_id,

        topic=topic.topic_name,

        duration_minutes=data.time_taken_minutes,

        quiz_score=data.score,

        revision=False,

        notes="Generated from quiz attempt"

    )


    create_learning_event(
        db,
        event
    )


    return attempt