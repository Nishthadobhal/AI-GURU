from app.models.learning_event import LearningEvent

def build_feature_vector(events):

    if len(events) == 0:

        return {
            "average_score": 0,
            "total_time": 0,
            "consistency": 0,
            "revision_count": 0,
            "activity_count": 0
        }


    total_score = 0

    total_time = 0

    revision_count = 0


    for event in events:


        total_score += event.quiz_score


        total_time += event.duration_minutes


        if event.revision:

            revision_count += 1



    average_score = (
        total_score / len(events)
    )


    consistency = min(
        len(events) / 10,
        1
    )


    return {

        "average_score": average_score / 100,


        "total_time": min(
            total_time / 500,
            1
        ),


        "revision_count": min(
            revision_count / 10,
            1
        ),


        "consistency": consistency,


        "activity_count": len(events)

    }