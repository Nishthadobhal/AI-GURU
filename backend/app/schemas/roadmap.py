from pydantic import BaseModel
from typing import List


class RoadmapTopicCreate(BaseModel):

    topic_name: str

    order: int



class RoadmapCreate(BaseModel):

    learning_goal_id: int

    title: str

    topics: List[RoadmapTopicCreate]



class RoadmapTopicResponse(BaseModel):

    id: int

    topic_name: str

    order: int

    completed: bool


    class Config:
        from_attributes = True



class RoadmapResponse(BaseModel):

    id: int

    learning_goal_id: int

    title: str

    topics: List[RoadmapTopicResponse]


    class Config:
        from_attributes = True