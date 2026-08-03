from sqlalchemy.orm import Session
from app.models.roadmap_topic import RoadmapTopic
from app.models.quiz import Quiz

from app.services.ai_quiz_service import generate_quiz_from_ai
from app.models.learning_event import LearningEvent

from app.services.pipeline_service import process_learning_update

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

    # Quiz already exists
    if quizzes:
        return quizzes

    print(f"Generating AI Quiz for: {topic.topic_name}")

    result = generate_quiz_from_ai(

        db=db,

        topic_id=topic_id,

        difficulty="medium",

        number_of_questions=5

    )

    print(result)

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

        print("-------------------------")
        print("Question ID:", question.id)
        print("Selected:", selected_answer)
        print("Correct :", question.correct_answer)

        answer_map_backend = {
            "option_a": "A",
            "option_b": "B",
            "option_c": "C",
            "option_d": "D"
}

        mapped_answer = answer_map_backend.get(selected_answer)

        if (
           selected_answer == question.correct_answer
           or
           mapped_answer == question.correct_answer
):
           print("MATCH")
           correct_answers += 1
        else:
            print("NOT MATCH")
        

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

    # ----------------------------
# Create Learning Event
# ----------------------------

    quiz = (
       db.query(Quiz)
       .filter(Quiz.id == data.quiz_id)
       .first()
)

    topic = (
        db.query(RoadmapTopic)
        .filter(RoadmapTopic.id == quiz.topic_id)
        .first()
)

    learning_event = LearningEvent(

        student_id=data.student_id,

        topic=topic.topic_name,

        duration_minutes=data.time_taken_minutes,

        quiz_score=score,

        revision=False,

        notes=""

)

    db.add(learning_event)

    db.commit()

    db.refresh(learning_event)

    process_learning_update(
        db,
        data.student_id
)

  

    # ----------------------------
# Update Roadmap Progress
# ----------------------------

    if score >= 70:

       quiz = (
           db.query(Quiz)
           .filter(
               Quiz.id == data.quiz_id
        )
            .first()
    )

       if quiz:

           topic = (
               db.query(RoadmapTopic)
               .filter(
                  RoadmapTopic.id == quiz.topic_id
            )
                .first()
        )

           if topic:

              topic.completed = True

              db.commit()

    return {
        "score": score,
        "total_questions": total_questions,
        "correct_answers": correct_answers
    }