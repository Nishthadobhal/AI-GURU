from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState

from app.models.learning_event import LearningEvent

from app.services.recommendation_service import (
    next_best_action
)


def get_dashboard(
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


    events = (
        db.query(LearningEvent)
        .filter(
            LearningEvent.student_id == student_id
        )
        .all()
    )


    if state:

        readiness = (
            state.buddhi
            + state.smriti
            + state.dharana
        ) / 3


        recommendation = next_best_action(
            {
                "buddhi": state.buddhi,
                "smriti": state.smriti,
                "dharana": state.dharana,
                "guna": state.guna
            },
            readiness
        )


    else:

        readiness = None

        recommendation = None


    return {

        "learner_state": state,

        "readiness": readiness,

        "total_learning_events": len(events),

        "recommendation": recommendation

    }