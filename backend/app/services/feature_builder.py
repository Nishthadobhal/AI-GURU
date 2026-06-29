from app.models.learning_event import LearningEvent


def build_feature_vector(events: list[LearningEvent]):
    total_sessions = len(events)

    total_study_time = 0
    total_quiz_score = 0
    revision_count = 0

    for event in events:
        total_study_time += event.duration_minutes

        if event.quiz_score is not None:
            total_quiz_score += event.quiz_score

        if event.revision:
            revision_count += 1

    average_quiz_score = (
        total_quiz_score / total_sessions
        if total_sessions > 0
        else 0
    )

    revision_rate = (
        revision_count / total_sessions
        if total_sessions > 0
        else 0
    )

    average_time = (
        total_study_time / total_sessions
        if total_sessions > 0
        else 0
    )

    return {
        "total_sessions": total_sessions,
        "total_study_time": total_study_time,
        "average_time": average_time,
        "average_quiz_score": average_quiz_score,
        "revision_rate": revision_rate
    }