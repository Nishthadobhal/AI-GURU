from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.learner_state import LearnerState


def get_student_analysis(
    db: Session,
    student_id: int
):

    state = (
        db.query(LearnerState)
        .filter(
            LearnerState.student_id == student_id
        )
        .first()
    )

    if state is None:

        raise HTTPException(
            status_code=404,
            detail="Learner state not found"
        )

    scores = {
        "Buddhi": state.buddhi,
        "Smriti": state.smriti,
        "Dharana": state.dharana,
        "Shila": state.shila,
        "Karma": state.karma,
        "Manasika": state.manasika,
        "Viveka": state.viveka,
        "Ruchi": state.ruchi,
        "Adaptability": state.adaptability
    }

    strongest_area = max(
        scores,
        key=scores.get
    )

    weakest_area = min(
        scores,
        key=scores.get
    )

    average = sum(scores.values()) / len(scores)

    if average >= 0.75:

        overall_level = "Advanced"

    elif average >= 0.50:

        overall_level = "Intermediate"

    else:

        overall_level = "Beginner"

    return {

        "strongest_area": strongest_area,

        "weakest_area": weakest_area,

        "overall_level": overall_level

    }