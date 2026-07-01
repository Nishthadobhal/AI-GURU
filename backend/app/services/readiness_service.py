def calculate_readiness(state):
    """
    Calculate overall readiness score.
    """

    buddhi = state["buddhi"]
    smriti = state["smriti"]
    dharana = state["dharana"]

    # Equal weights for MVP
    readiness = (
        buddhi +
        smriti +
        dharana
    ) / 3

    return round(readiness, 2)