from sqlalchemy.orm import Session

from app.models.roadmap import Roadmap

from app.models.roadmap_topic import RoadmapTopic

from app.models.learning_goal import LearningGoal

def create_roadmap(
    db: Session,
    data
):

    roadmap = Roadmap(
        learning_goal_id=data.learning_goal_id,
        title=data.title
    )


    db.add(roadmap)

    db.commit()

    db.refresh(roadmap)


    for topic in data.topics:

        roadmap_topic = RoadmapTopic(
            roadmap_id=roadmap.id,
            topic_name=topic.topic_name,
            order=topic.order
        )

        db.add(roadmap_topic)


    db.commit()

    db.refresh(roadmap)


    return roadmap




def get_student_roadmap(
    db: Session,
    student_id: int
):
    goal = (
        db.query(LearningGoal)
        .filter(LearningGoal.student_id == student_id)
        .first()
    )

    if not goal:
        return None

    roadmap = (
        db.query(Roadmap)
        .filter(Roadmap.learning_goal_id == goal.id)
        .first()
    )

    if not roadmap:
        return None

    topics = (
        db.query(RoadmapTopic)
        .filter(RoadmapTopic.roadmap_id == roadmap.id)
        .order_by(RoadmapTopic.order)
        .all()
    )

    completed_topics = [
        topic.topic_name
        for topic in topics
        if topic.completed
    ]

    pending_topics = [
        topic.topic_name
        for topic in topics
        if not topic.completed
    ]

    current_topic = (
        pending_topics[0]
        if pending_topics
        else None
    )

    return {
        "completed_topics": completed_topics,
        "pending_topics": pending_topics,
        "current_topic": current_topic
    }