from pydantic import BaseModel

class LearningGoalCreate(BaseModel):
    student_id:int
    goal_name:str
    level:str|None=None

class LearningGoalResponse(BaseModel):
    id:int
    student_id:int
    goal_name:str
    level:str|None

    class config:
        from_attributes=True
