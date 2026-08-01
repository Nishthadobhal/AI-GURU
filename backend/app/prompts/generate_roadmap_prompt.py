def build_generate_roadmap_prompt(
    student,
    goal
):
    return f"""
You are an expert AI curriculum designer.

Generate a personalized learning roadmap.

Student Name:
{student.name}

Learning Goal:
{goal}

Learning Style:
{student.learning_style}

Requirements:

1. Create an 8-week roadmap.
2. Each week must contain:
   - Week Number
   - Topic
   - Description
3. Topics must follow prerequisite order.
4. Keep roadmap practical.
5. Return ONLY valid JSON.

Output format:

{{
  "title":"{goal} Roadmap",
  "weeks":[
    {{
      "week":1,
      "topic":"...",
      "description":"..."
    }}
  ]
}}

Do not return markdown.

Do not return explanation.

Return JSON only.
"""