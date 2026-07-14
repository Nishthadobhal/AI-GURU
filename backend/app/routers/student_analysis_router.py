from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.student_analysis import StudentAnalysis

from app.services.student_analysis_service import (
    get_student_analysis
)

router = APIRouter(
    prefix="/student-analysis",
    tags=["Student Analysis"]
)


@router.get(
    "/{student_id}",
    response_model=StudentAnalysis
)
def student_analysis(
    student_id: int,
    db: Session = Depends(get_db)
):

    return get_student_analysis(
        db,
        student_id
    )