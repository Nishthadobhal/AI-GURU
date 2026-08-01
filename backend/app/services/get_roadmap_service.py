from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.learning_goal import LearningGoal
from app.models.roadmap import Roadmap
from app.models.roadmap_topic import RoadmapTopic


def get_student_roadmap(
    db: Session,
    student_id: int
):

    learning_goal = (
        db.query(LearningGoal)
        .filter(
            LearningGoal.student_id == student_id
        )
        .first()
    )

    if learning_goal is None:
        raise HTTPException(
            status_code=404,
            detail="Learning Goal not found"
        )

    roadmap = (
        db.query(Roadmap)
        .filter(
            Roadmap.learning_goal_id == learning_goal.id
        )
        .first()
    )

    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found"
        )

    topics = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.roadmap_id == roadmap.id
        )
        .order_by(RoadmapTopic.order)
        .all()
    )

    return {
        "title": roadmap.title,
        "weeks": [
            {   
                "id": topic.id,   
                "week": topic.order,
                "topic": topic.topic_name,
                "description": topic.description,
                "completed": topic.completed
            }
            for topic in topics
        ]
    }