from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.quiz_attempt import QuizAttempt
from app.models.quiz import Quiz
from app.models.roadmap_topic import RoadmapTopic


def get_weak_topics(
    db: Session,
    student_id: int
):

    results = (
        db.query(
            RoadmapTopic.topic_name,
            func.avg(QuizAttempt.score).label("average_score")
        )
        .join(Quiz, Quiz.topic_id == RoadmapTopic.id)
        .join(QuizAttempt, QuizAttempt.quiz_id == Quiz.id)
        .filter(QuizAttempt.student_id == student_id)
        .group_by(RoadmapTopic.topic_name)
        .all()
    )
    print("Results:", results)
    weak_topics = []

    for topic_name, average_score in results:
        WEAK_TOPIC_THRESHOLD = 70

        if average_score < WEAK_TOPIC_THRESHOLD:


            weak_topics.append(
                {
                    "topic": topic_name,
                    "average_score": round(float(average_score), 2)
                }
            )

    return {
        "student_id": student_id,
        "weak_topics": weak_topics
    }