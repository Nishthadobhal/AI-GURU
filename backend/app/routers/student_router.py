from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import (
    create_student,
    get_student,
    get_student_learning_events
)
router=APIRouter()


@router.post("/students")
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)

@router.get("/students/{student_id}")
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