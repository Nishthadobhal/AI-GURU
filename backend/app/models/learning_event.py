from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class LearningEvent(Base):
    __tablename__ = "learning_events"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    topic = Column(String, nullable=False)

    duration_minutes = Column(Integer, nullable=False)

    quiz_score = Column(Float)

    revision = Column(Boolean, default=False)

    notes = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship(
        "Student",
        back_populates="learning_events"
    )