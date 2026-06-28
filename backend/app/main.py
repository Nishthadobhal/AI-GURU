from fastapi import Depends, FastAPI,HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import (
    create_student,
    get_student,
    get_student_learning_events
)
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

@app.get("/students/{student_id}")
def get_student_details(
    student_id:int,
    db:Session=Depends(get_db)
):
    student = get_student(db, student_id)

    if student is None:
       raise HTTPException(
         status_code=404,
         detail="Student not found"
       )

    return student

@app.get("/student/{student_id}/learning-events")
def get_learning_events(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_student_learning_events(
        db,
        student_id
    )