from sqlalchemy.orm import Session

from app.models.roadmap import Roadmap

from app.models.roadmap_topic import RoadmapTopic



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