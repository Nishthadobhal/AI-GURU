from sqlalchemy.orm import Session

from app.models.student_profile import StudentProfile

def create_profile(
        db:Session,
        data
):
    profile=StudentProfile(
        student_id=data.student_id,
        student_type=data.student_type
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile