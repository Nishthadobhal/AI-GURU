import json

from sqlalchemy.orm import Session

from app.models.quiz import Quiz
from app.models.question import Question
from app.models.roadmap_topic import RoadmapTopic

from app.services.gemini_service import ask_gemini


def generate_quiz_from_ai(
    db: Session,
    topic_id: int,
    difficulty: str,
    number_of_questions: int
):

    topic = (
        db.query(RoadmapTopic)
        .filter(RoadmapTopic.id == topic_id)
        .first()
    )

    if not topic:
        return None
    
    prompt = f"""
Create {number_of_questions} MCQs about {topic.topic_name}.

Return ONLY JSON in this format:

[
  {{
    "question": "",
    "option_a": "",
    "option_b": "",
    "option_c": "",
    "option_d": "",
    "correct_answer": ""
  }}
]
"""

   
    print("\n========== PROMPT ==========")
    print(prompt)
    print("============================\n")


    response = ask_gemini(prompt)

    print("Gemini Response:")
    print(response)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        questions = json.loads(response)

    except json.JSONDecodeError:

        return {
            "success": False,
            "message": "Gemini returned invalid JSON.",
            "response": response
        }

    quiz = Quiz(
        topic_id=topic_id,
        title=f"{topic.topic_name} AI Quiz",
        difficulty=difficulty
    )

    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    required_keys = [
        "question",
        "option_a",
        "option_b",
        "option_c",
        "option_d",
        "correct_answer"
    ]

    for q in questions:

        if not all(key in q for key in required_keys):

            return {
                "success": False,
                "message": "Invalid question format returned by Gemini.",
                "question": q
            }

        question = Question(
            quiz_id=quiz.id,
            question_text=q["question"],
            option_a=q["option_a"],
            option_b=q["option_b"],
            option_c=q["option_c"],
            option_d=q["option_d"],
            correct_answer=q["correct_answer"]
        )

        db.add(question)

    db.commit()

    return {
        "success": True,
        "message": "AI Quiz Generated Successfully",
        "quiz_id": quiz.id,
        "topic": topic.topic_name,
        "difficulty": difficulty,
        "questions_created": len(questions)
    }