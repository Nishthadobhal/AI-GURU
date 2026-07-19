from sqlalchemy.orm import Session

from app.models.learner_state import LearnerState
from app.models.learning_event import LearningEvent
from app.models.roadmap_topic import RoadmapTopic
from app.models.learning_goal import LearningGoal
from app.models.roadmap import Roadmap

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

    # -----------------------------
    # Student Roadmap Progress
    # -----------------------------

    goal = (
        db.query(LearningGoal)
        .filter(
            LearningGoal.student_id == student_id
        )
        .first()
    )

    roadmap = None
    roadmap_topics = []

    if goal:
        roadmap = (
            db.query(Roadmap)
            .filter(
                Roadmap.learning_goal_id == goal.id
            )
            .first()
        )

    if roadmap:
        roadmap_topics = (
            db.query(RoadmapTopic)
            .filter(
                RoadmapTopic.roadmap_id == roadmap.id
            )
            .all()
        )

    completed_topics = [
        topic.topic_name
        for topic in roadmap_topics
        if topic.completed
    ]

    total_topics = len(roadmap_topics)

    progress = (
        len(completed_topics) / total_topics
        if total_topics > 0
        else 0
    )

    # -----------------------------
    # Readiness
    # -----------------------------

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