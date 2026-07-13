def next_best_action(
    state,
    readiness
):


    suggestions = []


    if state["buddhi"] < 0.5:

        suggestions.append(
            "Focus on understanding concepts deeply before moving ahead."
        )


    if state["smriti"] < 0.5:

        suggestions.append(
            "Revise previous topics to strengthen memory retention."
        )


    if state["dharana"] < 0.5:

        suggestions.append(
            "Try shorter focused learning sessions to improve concentration."
        )


    if state["shila"] < 0.5:

        suggestions.append(
            "Build a more consistent study routine."
        )


    if state["karma"] < 0.5:

        suggestions.append(
            "Increase practice and hands-on activities."
        )


    if state["viveka"] < 0.5:

        suggestions.append(
            "Spend more time analysing mistakes and solutions."
        )


    if state["adaptability"] < 0.5:

        suggestions.append(
            "Try mixed difficulty questions to improve adaptability."
        )


    if state["guna"] == "tamas":

        suggestions.append(
            "Start with small achievable goals to regain learning momentum."
        )


    elif state["guna"] == "rajas":

        suggestions.append(
            "Maintain balance between speed and depth of learning."
        )


    elif state["guna"] == "sattva":

        suggestions.append(
            "You are progressing steadily. Continue your learning path."
        )


    if readiness > 0.8:

        suggestions.append(
            "You are ready for advanced topics."
        )


    return suggestions