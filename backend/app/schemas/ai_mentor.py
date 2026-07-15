from pydantic import BaseModel

class AIMentorRequest(BaseModel):
    student_id:int
    question:str

class AIMentorResponse(BaseModel):
    answer:str