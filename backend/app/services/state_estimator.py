def estimate_state(features):
    average_quiz = features["average_quiz_score"]
    average_time = features["average_time"]

    # Buddhi
    buddhi = average_quiz

    # Dharana
    if average_time >= 90:
        dharana = 1.0
    elif average_time >= 45:
        dharana = 0.7
    else:
        dharana = 0.4

    return {
        "buddhi": buddhi,
        "dharana": dharana
    }