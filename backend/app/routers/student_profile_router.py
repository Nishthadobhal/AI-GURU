from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.student_profile import (
    StudentProfileCreate,
    StudentProfileResponse
)

from app.services.student_profile_service import (
    create_profile
)


router = APIRouter(
    prefix="/student-profile",
    tags=["Student Profile"]
)


@router.post(
    "",
    response_model=StudentProfileResponse
)
def add_profile(
    profile: StudentProfileCreate,
    db: Session = Depends(get_db)
):

    return create_profile(
        db,
        profile
    )