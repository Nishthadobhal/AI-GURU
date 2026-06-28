from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import create_student
from app.schemas.learning_event import LearningEventCreate
from app.services.learning_event_service import create_learning_event

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Guru Backend Running"}


@app.post("/students")
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)

@app.post("/learning-events")
def add_learning_event(
    learning_event: LearningEventCreate,
    db: Session = Depends(get_db)
):
    return create_learning_event(db, learning_event)