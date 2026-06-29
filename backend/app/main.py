from fastapi import FastAPI
from app.routers.student_router import router as student_router
from app.routers.analytics_router import (
    router as analytics_router
)
from app.models.learner_state import LearnerState
from app.routers.learning_event_router import (
    router as learning_event_router
)
from app.routers.learner_state_router import (
    router as learner_state_router
)

app = FastAPI()
app.include_router(student_router)
app.include_router(learning_event_router)
app.include_router(analytics_router)
app.include_router(learner_state_router)
@app.get("/")
def home():
    return {"message": "AI Guru Backend Running"}
