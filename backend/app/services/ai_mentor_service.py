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
    print(
    "Question Type:",
    question_type
)

    prompt = build_ai_prompt(

        context["student"],

        context["goal"],

        context["state"],

        context["dashboard"],

        context["conversations"],

        question

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