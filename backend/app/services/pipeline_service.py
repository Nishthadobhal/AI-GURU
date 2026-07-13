from sqlalchemy.orm import Session

from app.models.learning_event import LearningEvent
from app.models.learner_state import LearnerState

from app.services.feature_builder import build_feature_vector
from app.services.state_estimator import estimate_state


def process_learning_update(
    db: Session,
    student_id: int,
):

    # Get all learning events of this student
    events = (
        db.query(LearningEvent)
        .filter(LearningEvent.student_id == student_id)
        .all()
    )

    # Build feature vector
    features = build_feature_vector(events)

    # Estimate learner state
    state = estimate_state(features)

    # Check if learner state already exists
    db_state = (
        db.query(LearnerState)
        .filter(LearnerState.student_id == student_id)
        .first()
    )

    # Create new state
    if db_state is None:

        db_state = LearnerState(
            student_id=student_id,
            buddhi=state["buddhi"],
            smriti=state["smriti"],
            dharana=state["dharana"],
            guna=state["guna"],
            sattva=state["sattva"],
            rajas=state["rajas"],
            tamas=state["tamas"],

            shila=state["shila"],
            karma=state["karma"],
            manasika=state["manasika"],
            viveka=state["viveka"],
            ruchi=state["ruchi"],
            adaptability=state["adaptability"]
        )

        db.add(db_state)

    # Update existing state
    else:

        db_state.buddhi = state["buddhi"]
        db_state.smriti = state["smriti"]
        db_state.dharana = state["dharana"]
        db_state.guna = state["guna"]
        db_state.sattva = state["sattva"]
        db_state.rajas = state["rajas"]
        db_state.tamas = state["tamas"]

        db_state.shila = state["shila"]
        db_state.karma = state["karma"]
        db_state.manasika = state["manasika"]
        db_state.viveka = state["viveka"]
        db_state.ruchi = state["ruchi"]
        db_state.adaptability = state["adaptability"]

    db.commit()
    db.refresh(db_state)

    return db_state