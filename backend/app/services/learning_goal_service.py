from sqlalchemy.orm import Session
from app.models.learning_goal import LearningGoal

def create_learning_goal(
        db:Session,
        data
):
    goal=LearningGoal(
        student_id=data.student_id,
        goal_name=data.goal_name,
        level=data.level
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal