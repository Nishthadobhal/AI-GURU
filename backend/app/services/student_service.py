from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        goal=student.goal,
        learning_style=student.learning_style
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student