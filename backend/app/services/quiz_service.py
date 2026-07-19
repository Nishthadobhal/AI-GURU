from sqlalchemy.orm import Session

from app.models.quiz import Quiz


def create_quiz(
    db: Session,
    data
):

    quiz = Quiz(
        topic_id=data.topic_id,
        title=data.title,
        difficulty=data.difficulty
    )


    db.add(quiz)

    db.commit()

    db.refresh(quiz)


    return quiz

from app.models.roadmap_topic import RoadmapTopic


def get_quizzes_by_topic(
    db: Session,
    topic_id: int
):

    topic = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.id == topic_id
        )
        .first()
    )

    if not topic:
        return []

    quizzes = (
        db.query(Quiz)
        .filter(
            Quiz.topic_id == topic_id
        )
        .all()
    )

    return quizzes