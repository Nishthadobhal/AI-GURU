from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class StudentProfile(Base):
    __tablename__="student_profiles"
    
    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id=Column(
        Integer,
        ForeignKey("students.id"),
        unique=True,
        nullable=False
    )


    student_type = Column(
        String,
        nullable=False
    )

    current_level = Column(
        String
    )

    student = relationship(
        "Student",
        back_populates="profile"
    )

