def next_best_action(state, readiness):

    if readiness < 0.4:
        return "Revise previous topics."

    elif readiness < 0.7:
        if state["smriti"] < 0.5:
            return "Revise previous topics to improve retention."

        return "Practice more questions before moving ahead."

    else:
        if state["dharana"] < 0.7:
            return "Increase your focus with shorter study sessions."

        return "Proceed to the next topic."