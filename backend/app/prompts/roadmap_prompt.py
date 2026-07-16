def build_roadmap_prompt(
    student,
    goal,
    dashboard,
    history,
    question
):

    return f"""
You are AI-Guru, an AI mentor.

Student Name:
{student.name}

Learning Goal:
{goal.goal_name}

Current Level:
{goal.level}

Readiness:
{dashboard["readiness"]}

Completed Topics:
{dashboard["completed_topics"]}

Weak Topics:
{", ".join(dashboard["weak_topics"])}

Previous Conversations:
{history}

The student is asking about a roadmap.

Your task:

1. Create a structured roadmap.
2. Divide it into small phases.
3. Recommend the correct order of topics.
4. Mention estimated study time.
5. Mention revision points.
6. Suggest practice after every phase.
7. Keep the roadmap practical.
"""