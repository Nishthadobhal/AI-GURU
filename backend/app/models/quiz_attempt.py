from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.database import Base
from app.models.quiz import Quiz

class QuizAttempt(Base):

    __tablename__ = "quiz_attempts"


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


    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
        nullable=False
    )


    score = Column(
        Float,
        nullable=False
    )


    time_taken_minutes = Column(
        Integer
    )


    attempted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    student = relationship(
        "Student",
        back_populates="quiz_attempts"
    )


    quiz = relationship(
        "Quiz"
    )