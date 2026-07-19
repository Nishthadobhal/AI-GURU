from app.prompts.general_prompt import (
    build_general_prompt
)

from app.prompts.roadmap_prompt import (
    build_roadmap_prompt
)
from app.prompts.dashboard_prompt import (
    build_dashboard_prompt
)

def build_ai_prompt(

    student,

    goal,

    state,

    dashboard,
    roadmap,

    conversations,

    question,

    question_type

):

    history = ""

    for chat in conversations:

        history += f"""
Question:
{chat.question}

Answer:
{chat.answer}

"""
    if question_type == "roadmap":

        return build_roadmap_prompt(
           student,
           goal,
           dashboard,
           roadmap,
           history,
           question
    )

    elif question_type == "dashboard":

       return build_dashboard_prompt(
           student,
           goal,
           state,
           dashboard,
           roadmap,
           history,
           question
    )

    return build_general_prompt(
       student,
       goal,
       state,
       dashboard,
       roadmap,
       history,
       question
)    



    