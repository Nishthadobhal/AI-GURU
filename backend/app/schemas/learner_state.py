from pydantic import BaseModel


class LearnerStateResponse(BaseModel):
    buddhi: float
    smriti: float
    dharana: float
    guna: float

    class Config:
        from_attributes = True