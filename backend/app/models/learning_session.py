from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class LearningSession(Base):

    __tablename__ = "learning_sessions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )


    topic_id = Column(
        Integer,
        ForeignKey("roadmap_topics.id"),
        nullable=False
    )


    duration_minutes = Column(
        Integer,
        default=0
    )


    completed = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    student = relationship(
        "Student",
        back_populates="learning_sessions"
    )


    topic = relationship(
        "RoadmapTopic"
    )