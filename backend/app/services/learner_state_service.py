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

def update_learnner_state(
        db:Session,
        student_id:id
):
    events=get_learning_events_by_student(db,Session)
    features=build_feature_vector(events)
    state=estimate_state(features)
    db_state=(db.query(LearnerState).filter(LearnerState.student_id==student_id).first())
    if db_state is None:
        db_state=LearnerState(
            student_id=student_id,
            buddhi=state["buddhi"],
            smriti=state["smriti"],
            dharana=state["dharana"],
            guna=state["guna"]
        )
        db.add(db_state)
    else:   
     db_state.buddhi = state["buddhi"]
     db_state.smriti = state["smriti"]
     db_state.dharana = state["dharana"]
     db_state.guna = state["guna"]
    db.commit()
    db.refresh(db_state)
    return db_state