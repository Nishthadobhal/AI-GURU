def estimate_state(features):

    average_quiz = features["average_quiz_score"]
    average_time = features["average_time"]
    revision_rate = features["revision_rate"]

    # Buddhi (Understanding)
    buddhi = average_quiz / 100

    # Smriti (Retention)
    smriti = revision_rate

    # Dharana (Focus)
    if average_time >= 90:
        dharana = 1.0
    elif average_time >= 45:
        dharana = 0.7
    else:
        dharana = 0.4

    # Guna (Temporary MVP Score)
    guna = (
        buddhi +
        smriti +
        dharana
    ) / 3

    return {
        "buddhi": round(buddhi, 2),
        "smriti": round(smriti, 2),
        "dharana": round(dharana, 2),
        "guna": round(guna, 2)
    }