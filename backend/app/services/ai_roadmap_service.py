from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.models.student_profile import StudentProfile
from app.models.learner_state import LearnerState
from app.models.learning_goal import LearningGoal
from app.models.roadmap import Roadmap
from app.models.roadmap_topic import RoadmapTopic


def generate_ai_roadmap(
    db: Session,
    student_id: int,
    goal: str
):

    # ----------------------------
    # Student
    # ----------------------------
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # ----------------------------
    # Student Profile
    # ----------------------------
    profile = (
        db.query(StudentProfile)
        .filter(StudentProfile.student_id == student_id)
        .first()
    )

    # ----------------------------
    # Learner State
    # ----------------------------
    learner_state = (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )

    # ----------------------------
    # Learning Goal
    # ----------------------------
    learning_goal = (
        db.query(LearningGoal)
        .filter(
            LearningGoal.goal_name.ilike(f"%{goal}%")
        )
        .first()
    )

    if learning_goal is None:
        raise HTTPException(
            status_code=404,
            detail="Learning goal not found"
        )

    # ----------------------------
    # Roadmap
    # ----------------------------
    roadmap = (
        db.query(Roadmap)
        .filter(
            Roadmap.learning_goal_id == learning_goal.id
        )
        .first()
    )

    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found"
        )

    # ----------------------------
    # Topics
    # ----------------------------
    topics = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.roadmap_id == roadmap.id
        )
        .order_by(RoadmapTopic.id)
        .all()
    )

    result = []

    result.append(f"Goal : {goal}")

    if profile and profile.current_level:
        result.append(
            f"Current Level : {profile.current_level}"
        )

    result.append("")

    week = 1

    for topic in topics:

        result.append(
            f"Week {week}"
        )

        result.append(
            f"• {topic.topic_name}"
        )

        if learner_state:

            if learner_state.smriti < 0.5:

                result.append(
                    "  Revision after completing this topic."
                )

            if learner_state.dharana < 0.5:

                result.append(
                    "  Study this topic in 25-minute focus sessions."
                )

        result.append("")

        week += 1

    result.append("Take a complete mock quiz.")

    result.append("Review all weak topics.")

    return result