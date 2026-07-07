from pydantic import BaseModel


class StudentProfileCreate(BaseModel):

    student_id: int

    student_type: str


class StudentProfileResponse(BaseModel):

    id: int

    student_id: int

    student_type: str

    current_level: str | None


    class Config:
        from_attributes = True