from fastapi import FastAPI
from app.routers.student_router import router as student_router
from app.routers.analytics_router import (
    router as analytics_router
)

from app.routers.learning_event_router import (
    router as learning_event_router
)
from app.routers.learner_state_router import (
    router as learner_state_router
)
from app.routers.student_profile_router import router as student_profile_router
from app.routers.learning_goal_router import router as learning_goal_router
from app.routers.roadmap_router import router as roadmap_router
from app.routers.learning_session_router import (
    router as learning_session_router
)
from app.routers.quiz_attempt_router import (
    router as quiz_attempt_router
)
from app.routers.quiz_router import (
    router as quiz_router
)
from app.routers.dashboard_router import (
    router as dashboard_router
)
from app.routers.ai_roadmap_router import router as ai_roadmap_router
from app.routers.student_analysis_router import (
    router as student_analysis_router
)
from app.routers.gemini_router import (
    router as gemini_router
)
from app.routers.ai_mentor_router import (
    router as ai_mentor_router
)
app = FastAPI()
app.include_router(student_router)
app.include_router(learning_event_router)
app.include_router(learner_state_router)
app.include_router(analytics_router)
app.include_router(student_profile_router)
app.include_router(learning_goal_router)
app.include_router(roadmap_router)
app.include_router(learning_session_router)
app.include_router(quiz_attempt_router)
app.include_router(
    quiz_router
)
app.include_router(
    dashboard_router
)
app.include_router(ai_roadmap_router)
app.include_router(
    student_analysis_router
)
app.include_router(
    gemini_router
)
app.include_router(
    ai_mentor_router
)

@app.get("/")
def home():
    return {"message": "AI Guru Backend Running"}
