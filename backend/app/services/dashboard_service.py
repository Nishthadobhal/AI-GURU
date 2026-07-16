from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState
from app.models.learning_event import LearningEvent
from app.models.learning_session import LearningSession
from app.models.roadmap_topic import RoadmapTopic

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

    weak_topics = []

    for event in events:

        if event.quiz_score < 50:
            weak_topics.append(event.topic)

    weak_topics = list(set(weak_topics))

    sessions = (
        db.query(LearningSession)
        .filter(
            LearningSession.student_id == student_id
        )
        .all()
    )

    completed_topic_ids = {
        session.topic_id
        for session in sessions
        if session.completed
    }

    completed_topic_objects = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.id.in_(completed_topic_ids)
        )
        .all()
    )

    completed_topics = [
        topic.topic_name
        for topic in completed_topic_objects
    ]

    total_topics = (
        db.query(RoadmapTopic)
        .count()
    )

    progress = (
        len(completed_topics) / total_topics
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
                "guna": state.guna,
                "sattva": state.sattva,
                "rajas": state.rajas,
                "tamas": state.tamas,
                "shila": state.shila,
                "karma": state.karma,
                "manasika": state.manasika,
                "viveka": state.viveka,
                "ruchi": state.ruchi,
                "adaptability": state.adaptability
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

        "completed_topics_count": len(completed_topics),

        "total_topics": total_topics,

        "weak_topics": weak_topics,

        "total_learning_events": len(events),

        "recommendation": recommendation

    }