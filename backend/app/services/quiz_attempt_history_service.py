from sqlalchemy.orm import Session

from app.models.quiz_attempt import QuizAttempt
from app.models.quiz import Quiz


def get_quiz_attempt_history(
    db: Session,
    student_id: int
):

    attempts = (
        db.query(QuizAttempt, Quiz)
        .join(Quiz, QuizAttempt.quiz_id == Quiz.id)
        .filter(QuizAttempt.student_id == student_id)
        .order_by(QuizAttempt.attempted_at.desc())
        .all()
    )

    history = []

    for attempt, quiz in attempts:

        history.append(
            {
                "quiz_id": quiz.id,
                "quiz_title": quiz.title,
                "score": attempt.score,
                "attempted_at": attempt.attempted_at
            }
        )

    return history