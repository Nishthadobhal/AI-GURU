from app.services.feature_builder import build_feature_vector
from app.services.state_estimator import estimate_state
from app.services.recommendation_service import next_best_action
from app.services.topic_analyzer import analyze_topics
from app.services.consistency_service import calculate_consistency

def generate_student_report(events):
    features = build_feature_vector(events)

    topic_analysis=analyze_topics(events)

    consistency = calculate_consistency(events)

    state = estimate_state(features)

    recommendation = next_best_action(state)

    return {
        "features": features,
        "topic_analysis": topic_analysis,
        "consistency_score": consistency,
        "state": state,
        "recommendation": recommendation
    }