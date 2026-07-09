from sqlalchemy.orm import Session

from app.models.quiz import Quiz


def create_quiz(
    db: Session,
    data
):

    quiz = Quiz(
        topic_id=data.topic_id,
        title=data.title,
        difficulty=data.difficulty
    )


    db.add(quiz)

    db.commit()

    db.refresh(quiz)


    return quiz