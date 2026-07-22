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
You are AI-Guru, an intelligent and supportive learning mentor.

Your task is to generate a personalized {days}-day revision plan for the student based ONLY on the information provided below.

=========================
STUDENT INFORMATION
=========================

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

=========================
INSTRUCTIONS
=========================

1. Generate a realistic {days}-day revision plan.
2. Prioritize weak topics before introducing new topics.
3. Continue learning according to the roadmap.
4. Never skip prerequisite topics.
5. Give achievable daily tasks.
6. Include concept revision as well as coding practice.
7. Recommend suitable DSA/algorithm practice problems wherever appropriate.
8. Allocate study workload based on:
   - Readiness Score
   - Weak Topics
   - Remaining Roadmap
   - Number of Days
9. Reserve the final day for revision and a mock test.
10. Keep the plan motivating and practical.

=========================
IMPORTANT RULES
=========================

- Use ONLY the roadmap provided above.
- Do NOT invent completed topics.
- Do NOT invent future topics.
- Do NOT introduce topics outside the roadmap.
- If a topic is already completed, include it only for revision if it is a weak topic.
- If there are no weak topics, continue with the roadmap naturally.
- Do NOT explicitly mention whether weak topics exist or not.
- Do NOT change the roadmap order.
- Base every recommendation only on the student's dashboard and roadmap.
- Avoid generic advice that is unrelated to the student's progress.

=========================
OUTPUT FORMAT
=========================

Return the response in Markdown using the following structure.

# Personalized Revision Plan

## Student Summary
- Learning Goal
- Readiness Score
- Current Topic
- Focus Areas

## Day 1
Goal:
Topics:
Tasks:
Practice Problems:
Estimated Study Time:

## Day 2
Goal:
Topics:
Tasks:
Practice Problems:
Estimated Study Time:

Continue the same format until Day {days}.

## Final Day
- Complete revision
- Mock Test
- Self Evaluation

## AI-Guru Tips
Provide 3-5 personalized study tips based on the student's current progress.

Keep the response well-structured, easy to read, and encouraging.
"""
  
    revision_plan = ask_gemini(
        prompt
    )

    return {
        "revision_plan": revision_plan
    }