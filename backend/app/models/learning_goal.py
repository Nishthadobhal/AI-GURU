from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class LearningGoal(Base):

    __tablename__ = "learning_goals"


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


    goal_name = Column(
        String,
        nullable=False
    )


    level = Column(
        String
    )


    student = relationship(
        "Student",
        back_populates="learning_goals"
    )