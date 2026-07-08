from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    goal = Column(String, nullable=False)
    learning_style = Column(String, nullable=False)

    learning_events = relationship(
        "LearningEvent",
        back_populates="student"
    )

    learner_state = relationship(
       "LearnerState",
       back_populates="student",
       uselist=False
    )
    profile = relationship(
    "StudentProfile",
    back_populates="student",
    uselist=False
)
    learning_goals = relationship(
    "LearningGoal",
    back_populates="student"
)
    learning_sessions = relationship(
    "LearningSession",
    back_populates="student"
)