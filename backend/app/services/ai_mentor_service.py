from sqlalchemy.orm import Session

from app.services.student_context_service import (
    get_student_context
)

from app.services.prompt_builder import (
    build_ai_prompt
)

from app.services.gemini_service import (
    ask_gemini
)

from app.schemas.conversation import (
    ConversationCreate
)

from app.services.conversation_service import (
    save_conversation
)
from app.services.question_classifier import (
    classify_question
)

def ask_ai_mentor(
    db: Session,
    student_id: int,
    question: str
):

    context = get_student_context(
        db,
        student_id
    )

    question_type = classify_question(
        question
    )

    print("Question Type:", question_type)

    print("Dashboard =", context["dashboard"])
    print(
        "Completed Topics =",
        context["dashboard"].get("completed_topics")
    )
    print(
        "Completed Type =",
        type(context["dashboard"].get("completed_topics"))
    )
    print(
        "Weak Topics =",
        context["dashboard"].get("weak_topics")
    )
    print(
        "Weak Type =",
        type(context["dashboard"].get("weak_topics"))
    )

    prompt = build_ai_prompt(
        context["student"],
        context["goal"],
        context["state"],
        context["dashboard"],
        context["conversations"],
        question,
        question_type
    )

    answer = ask_gemini(
        prompt
    )

    conversation = ConversationCreate(

        student_id=student_id,

        question=question,

        answer=answer

    )

    save_conversation(
        db,
        conversation
    )

    return answer