import json

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.models.learning_goal import LearningGoal
from app.models.roadmap import Roadmap
from app.models.roadmap_topic import RoadmapTopic

from app.prompts.generate_roadmap_prompt import (
    build_generate_roadmap_prompt
)

from app.services.gemini_service import ask_gemini


def clean_json(text: str):

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def generate_ai_roadmap(
    db: Session,
    student_id: int,
    goal: str
):

    # ----------------------------
    # Fetch Student
    # ----------------------------
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # ----------------------------
    # Fetch Learning Goal
    # ----------------------------
    learning_goal = (
        db.query(LearningGoal)
        .filter(
            LearningGoal.student_id == student_id,
            LearningGoal.goal_name == goal
        )
        .first()
    )

    if learning_goal is None:
        raise HTTPException(
            status_code=404,
            detail="Learning Goal not found"
        )

    # ----------------------------
    # Build Prompt
    # ----------------------------
    prompt = build_generate_roadmap_prompt(
        student,
        goal
    )

    # ----------------------------
    # Gemini Response
    # ----------------------------
    response = ask_gemini(prompt)

    if "Gemini server is busy" in response:
        raise HTTPException(
            status_code=503,
            detail="Gemini is temporarily unavailable. Please try again."
        )

    print("\n========== GEMINI RAW RESPONSE ==========\n")
    print(response)
    print("\n=========================================\n")

    # ----------------------------
    # Clean Response
    # ----------------------------
    response = clean_json(response)

    # ----------------------------
    # Parse JSON
    # ----------------------------
    try:

        roadmap = json.loads(response)
        print("JSON Parsed Successfully")

        print("Saving Roadmap...")

        print(roadmap)

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Gemini returned invalid JSON"
        )

    # ----------------------------
    # Delete old roadmap (optional)
    # ----------------------------
    old_roadmaps = (
        db.query(Roadmap)
        .filter(
            Roadmap.learning_goal_id == learning_goal.id
        )
        .all()
    )

    for old in old_roadmaps:

        db.query(RoadmapTopic).filter(
            RoadmapTopic.roadmap_id == old.id
        ).delete()

        db.delete(old)

    db.commit()
    print("Roadmap Saved Successfully")
    # ----------------------------
    # Save Roadmap
    # ----------------------------
    roadmap_db = Roadmap(

        learning_goal_id=learning_goal.id,

        title=roadmap["title"]

    )

    db.add(roadmap_db)

    db.commit()

    db.refresh(roadmap_db)

    # ----------------------------
    # Save Topics
    # ----------------------------
    saved_topics = []

    for week in roadmap["weeks"]:

        topic = RoadmapTopic(

            roadmap_id=roadmap_db.id,

            topic_name=week["topic"],

            description=week["description"],

            order=week["week"],

            completed=False

        )

        db.add(topic)
        saved_topics.append(topic)

    db.commit()

    


    
    print("Topics Saved Successfully")
    return roadmap