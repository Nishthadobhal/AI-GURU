def classify_question(question: str):

    question = question.lower()

    if "roadmap" in question:

        return "roadmap"

    elif "performance" in question or "dashboard" in question:

        return "dashboard"

    elif "recommend" in question or "weak" in question:

        return "recommendation"

    else:

        return "general"