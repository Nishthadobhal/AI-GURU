from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class LearnerState(Base):
    __tablename__ = "learner_states"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True,
        nullable=False
    )

    buddhi = Column(Float, default=0.0)

    smriti = Column(Float, default=0.0)

    dharana = Column(Float, default=0.0)

    guna = Column(Float, default=0.0)

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    student = relationship(
        "Student",
        back_populates="learner_state"
    )