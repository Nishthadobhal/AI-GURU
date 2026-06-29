from app.services.feature_builder import build_feature_vector
from app.services.state_estimator import estimate_state
from app.services.recommendation_service import next_best_action
from app.services.topic_analyzer import analyze_topics

def generate_student_report(events):
    features = build_feature_vector(events)

    topic_analysis=analyze_topics(events)

    state = estimate_state(features)

    recommendation = next_best_action(state)

    return {
        "features": features,
        "topic_analysis": topic_analysis,
        "state": state,
        "recommendation": recommendation
    }