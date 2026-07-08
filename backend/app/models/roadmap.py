from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Roadmap(Base):
    __tablename__="roadmaps"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    learning_goal_id=Column(
        Integer,
        ForeignKey("learning_goals.id"),
        nullable=False
    )

    title=Column(String,nullable=False)

    learning_goal=relationship(
        "LearningGoal",
        back_populates="roadmaps"
    )

    topics=relationship(
        "RoadmapTopic",
        back_populates="roadmap"
    )