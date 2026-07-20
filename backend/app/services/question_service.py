from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.quiz import Quiz

from fastapi import HTTPException


def create_question(
    db: Session,
    data
):

    quiz = (
        db.query(Quiz)
        .filter(
            Quiz.id == data.quiz_id
        )
        .first()
    )

    if not quiz:

        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    question = Question(
        quiz_id=data.quiz_id,
        question_text=data.question_text,
        option_a=data.option_a,
        option_b=data.option_b,
        option_c=data.option_c,
        option_d=data.option_d,
        correct_answer=data.correct_answer
    )

    db.add(question)

    db.commit()

    db.refresh(question)

    return question

from app.models.question import Question


def get_questions_by_quiz(
    db: Session,
    quiz_id: int
):

    questions = (
        db.query(Question)
        .filter(
            Question.quiz_id == quiz_id
        )
        .all()
    )

    return questions