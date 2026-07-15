from sqlalchemy.orm import Session

from app.models.conversation import Conversation

from app.schemas.conversation import ConversationCreate

def save_conversation(
        db:Session,
        data:ConversationCreate
):
    conversation=Conversation(
        student_id=data.student_id,
        question=data.question,
        answer=data.answer
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

def get_recent_conversation(
        db:Session,
        student_id=int,
        limit:int =5
):
    conversations=(
        db.query(Conversation)
        .filter(
            Conversation.student_id==student_id
        )
        .order_by(
            Conversation.created_at.desc()
        )
        .limit(limit)
        .all()
    )
    return conversations
    