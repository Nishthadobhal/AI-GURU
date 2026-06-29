from app.services.feature_builder import build_feature_vector
from app.services.state_estimator import estimate_state
from app.services.recommendation_service import next_best_action


# def generate_student_report(events):
#     features = build_feature_vector(events)

#     state = estimate_state(features)

#     recommendation = next_best_action(state)

#     return {
#         "features": features,
#         "state": state,
#         "recommendation": recommendation
#     }

def generate_student_report(events):
    features = build_feature_vector(events)

    print(features)   # <-- Add this

    state = estimate_state(features)

    recommendation = next_best_action(state)

    return {
        "features": features,
        "state": state,
        "recommendation": recommendation
    }