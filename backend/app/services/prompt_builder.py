def build_ai_prompt(

    student,

    goal,

    state,

    dashboard,

    conversations,

    question

):

    history = ""

    for chat in conversations:

        history += f"""
Question:
{chat.question}

Answer:
{chat.answer}

"""

    prompt = f"""
You are AI-Guru.

You are an intelligent mentor for engineering students.

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

Previous Conversations:
{history}

Student Question:
{question}

Give a personalized answer based on the student's profile, previous conversations, and learning progress.
Keep the answer practical, concise, and motivating.
"""

    return prompt