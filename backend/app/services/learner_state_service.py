from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState

from app.services.learning_event_service import (
    get_learning_events_by_student,
)

from app.services.feature_builder import (
    build_feature_vector,
)

from app.services.state_estimator import (
    estimate_state,
)

def get_learner_state(
    db: Session,
    student_id: int
):
    return (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )


def update_learner_state(
    db: Session,
    student_id: int,
    new_state: dict
):


    state = (
        db.query(LearnerState)
        .filter(
            LearnerState.student_id == student_id
        )
        .first()
    )


    if not state:


        state = LearnerState(
            student_id=student_id
        )


        db.add(state)



    state.buddhi = new_state["buddhi"]

    state.smriti = new_state["smriti"]

    state.dharana = new_state["dharana"]

    state.guna = new_state["guna"]


    state.sattva = new_state["sattva"]

    state.rajas = new_state["rajas"]

    state.tamas = new_state["tamas"]


    state.shila = new_state["shila"]

    state.karma = new_state["karma"]

    state.manasika = new_state["manasika"]

    state.viveka = new_state["viveka"]

    state.ruchi = new_state["ruchi"]

    state.adaptability = new_state["adaptability"]


    db.commit()

    db.refresh(state)


    return state