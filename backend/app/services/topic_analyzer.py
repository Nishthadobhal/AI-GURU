from collections import defaultdict
from app.models.learning_event import LearningEvent


def analyze_topics(events: list[LearningEvent]):
    topic_scores = defaultdict(list)

    for event in events:
        if event.quiz_score is not None:
            topic_scores[event.topic].append(event.quiz_score)

    average_scores = {}

    for topic, scores in topic_scores.items():
        average_scores[topic] = sum(scores) / len(scores)

    strong_topics = []
    weak_topics = []

    for topic, score in average_scores.items():
        if score >= 75:
            strong_topics.append(topic)
        else:
            weak_topics.append(topic)

    return {
        "strong_topics": strong_topics,
        "weak_topics": weak_topics
    }