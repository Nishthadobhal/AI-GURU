from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship

from app.database import Base


class RoadmapTopic(Base):

    __tablename__ = "roadmap_topics"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    roadmap_id = Column(
        Integer,
        ForeignKey("roadmaps.id"),
        nullable=False
    )


    topic_name = Column(
        String,
        nullable=False
    )


    order = Column(
        Integer
    )


    completed = Column(
        Boolean,
        default=False
    )


    roadmap = relationship(
        "Roadmap",
        back_populates="topics"
    )