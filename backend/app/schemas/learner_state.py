from pydantic import BaseModel

class LearnerStateResponse(BaseModel):
    student_id: int

    buddhi: float
    smriti: float
    dharana: float

    guna: str

    sattva: float
    rajas: float
    tamas: float

    shila: float
    karma: float
    manasika: float
    viveka: float
    ruchi: float
    adaptability: float

    class Config:
        from_attributes = True