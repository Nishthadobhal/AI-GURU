from app.services.feature_builder import build_feature_vector
from app.services.state_estimator import estimate_state
from app.services.recommendation_service import next_best_action
from app.services.topic_analyzer import analyze_topics
from app.services.consistency_service import calculate_consistency
from app.services.readiness_service import calculate_readiness

def generate_student_report(events):
    features = build_feature_vector(events)

    topic_analysis=analyze_topics(events)

    consistency = calculate_consistency(events)

    state = estimate_state(features)
    
    readiness=calculate_readiness(state)

    recommendation = next_best_action(state,readiness)

    return {
        "features": features,
        "topic_analysis": topic_analysis,
        "consistency_score": consistency,
        "state": state,
        "readiness":readiness,
        "recommendation": recommendation
    }