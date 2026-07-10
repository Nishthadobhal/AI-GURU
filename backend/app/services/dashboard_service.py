from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState

from app.models.learning_event import LearningEvent

from app.services.recommendation_service import (
    next_best_action
)

from app.models.roadmap_topic import RoadmapTopic

from app.models.learning_session import LearningSession

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

    weak_topics = []


    for event in events:

        if event.quiz_score < 50:

           weak_topics.append(
               event.topic
        )


    weak_topics = list(
        set(weak_topics)
)

    sessions = (
        db.query(LearningSession)
        .filter(
            LearningSession.student_id == student_id
    )
        .all()
)


    completed_topics = len(
        [
           s for s in sessions
           if s.completed
        ]
)


    total_topics = (
        db.query(RoadmapTopic)
        .count()
)


    progress = (
         completed_topics / total_topics
         if total_topics > 0
         else 0
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

        "progress": progress,

        "completed_topics": completed_topics,

        "total_topics": total_topics,
        "weak_topics": weak_topics,
        "total_learning_events": len(events),

        "recommendation": recommendation

    }