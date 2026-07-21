from sqlalchemy.orm import Session

from app.services.student_context_service import (
    get_student_context,
)

from app.services.gemini_service import (
    ask_gemini,
)
def generate_revision_plan(
    db: Session,
    student_id: int,
    days: int
):

    context = get_student_context(
        db,
        student_id
    )

    student = context["student"]
    goal = context["goal"]
    dashboard = context["dashboard"]
    roadmap = context["roadmap"]
    prompt = f"""
You are AI-Guru.

Create a personalized {days}-day revision plan.

Student Name:
{student.name}

Learning Goal:
{goal.goal_name}

Readiness Score:
{dashboard["readiness"]:.2f}

Completed Topics:
{", ".join(dashboard["completed_topics"]) if dashboard["completed_topics"] else "None"}

Weak Topics:
{", ".join(dashboard["weak_topics"]) if dashboard["weak_topics"] else "None"}

Current Topic:
{roadmap["current_topic"]}

Pending Topics:
{", ".join(roadmap["pending_topics"]) if roadmap["pending_topics"] else "None"}

Instructions:

1. Prioritize weak topics.
2. Continue following the roadmap.
3. Don't skip prerequisite topics.
4. Give realistic daily tasks.
5. Include revision and practice.
6. End with a mock test on the final day.
"""