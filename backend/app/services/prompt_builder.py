def build_ai_prompt(

    student,

    goal,

    state,

    dashboard,

    question

):

    prompt = f"""
You are AI-Guru.

You are an intelligent mentor.

Student Name:
{student.name}

Goal:
{goal.goal_name}

Current Level:
{goal.level}

Current Guna:
{state.guna}

Readiness:
{dashboard["readiness"]}

Completed Topics:
{dashboard["completed_topics"]}

Weak Topics:
{", ".join(dashboard["weak_topics"])}

Student Question:
{question}

Give a personalized answer.
"""

    return prompt