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

from app.models.roadmap_topic import RoadmapTopic


def get_quizzes_by_topic(
    db: Session,
    topic_id: int
):

    topic = (
        db.query(RoadmapTopic)
        .filter(
            RoadmapTopic.id == topic_id
        )
        .first()
    )

    if not topic:
        return []

    quizzes = (
        db.query(Quiz)
        .filter(
            Quiz.topic_id == topic_id
        )
        .all()
    )

    return quizzes

from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt


def submit_quiz(db: Session, data):

    questions = (
        db.query(Question)
        .filter(
            Question.quiz_id == data.quiz_id
        )
        .all()
    )

    if not questions:
        return None

    correct_answers = 0

    answer_map = {
        answer.question_id: answer.selected_answer
        for answer in data.answers
    }

    for question in questions:

        selected_answer = answer_map.get(question.id)

        if selected_answer == question.correct_answer:
            correct_answers += 1

    total_questions = len(questions)

    score = (correct_answers / total_questions) * 100

    attempt = QuizAttempt(
        student_id=data.student_id,
        quiz_id=data.quiz_id,
        score=score,
        time_taken_minutes=data.time_taken_minutes
    )

    db.add(attempt)

    db.commit()

    db.refresh(attempt)

    return {
        "score": score,
        "total_questions": total_questions,
        "correct_answers": correct_answers
    }