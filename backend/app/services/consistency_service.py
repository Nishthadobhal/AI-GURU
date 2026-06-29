from collections import Counter

from app.models.learning_event import LearningEvent


def calculate_consistency(events: list[LearningEvent]):
    if not events:
        return 0

    study_days = Counter()

    for event in events:
        day = event.created_at.date()
        study_days[day] += 1

    total_days = len(study_days)

    total_sessions = len(events)

    consistency_score = total_sessions / total_days

    return round(consistency_score, 2)