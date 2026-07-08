from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Quiz(Base):

    __tablename__ = "quizzes"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    topic_id = Column(
        Integer,
        ForeignKey("roadmap_topics.id"),
        nullable=False
    )


    title = Column(
        String,
        nullable=False
    )


    difficulty = Column(
        String,
        default="medium"
    )


    questions = relationship(
        "Question",
        back_populates="quiz"
    )