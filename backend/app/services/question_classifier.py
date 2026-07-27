def classify_question(question: str):

    question = question.lower()

    if any(word in question for word in [
        "roadmap", "next topic", "learning path"
    ]):
        return "roadmap"

    elif any(word in question for word in [
        "performance", "dashboard", "progress"
    ]):
        return "dashboard"

    elif any(word in question for word in [
        "recommend", "weak", "improve"
    ]):
        return "recommendation"

    else:
        return "general"