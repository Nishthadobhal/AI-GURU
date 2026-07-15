from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Conversation(Base):
    __tablename__="conversations"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )
    student_id=Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )
    question=Column(
        Text,
        nullable=False
    )
    answer=Column(
        Text,
        nullable=False
    )
    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )
    student=relationship(
        "student",
        back_populates="conversations"
    )