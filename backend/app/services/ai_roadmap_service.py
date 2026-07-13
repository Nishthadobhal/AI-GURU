from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.models.student_profile import StudentProfile
from app.models.learner_state import LearnerState


def generate_ai_roadmap(
    db: Session,
    student_id: int,
    goal: str
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    profile = (
        db.query(StudentProfile)
        .filter(StudentProfile.student_id == student_id)
        .first()
    )

    learner_state = (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )

    roadmap = []

    roadmap.append(f"Goal: {goal}")

    if profile:
        roadmap.append(
            f"Current Level: {profile.current_level}"
        )

    if learner_state:

        if learner_state.buddhi < 0.5:
            roadmap.append(
                "Revise the fundamentals before learning new topics."
            )

        if learner_state.smriti < 0.5:
            roadmap.append(
                "Schedule revision after every study session."
            )

        if learner_state.dharana < 0.5:
            roadmap.append(
                "Study in short 25-minute focused sessions."
            )

        if learner_state.guna == "tamas":
            roadmap.append(
                "Start with easy topics to build momentum."
            )

        elif learner_state.guna == "rajas":
            roadmap.append(
                "Balance speed with conceptual understanding."
            )

        elif learner_state.guna == "sattva":
            roadmap.append(
                "You are ready to learn progressively challenging topics."
            )

    roadmap.append(
        "Complete quizzes after every topic."
    )

    roadmap.append(
        "Review weak topics every weekend."
    )

    return roadmap