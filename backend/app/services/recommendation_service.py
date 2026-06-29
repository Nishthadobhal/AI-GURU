def next_best_action(state):
    if state["buddhi"] < 0.5:
        return "Revise previous topics."

    if state["dharana"] < 0.5:
        return "Take shorter focused study sessions."

    return "Proceed to the next topic."