from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.ai_roadmap import (
    AIRoadmapRequest,
    AIRoadmapResponse
)

from app.services.ai_roadmap_service import (
    generate_ai_roadmap
)

router = APIRouter(
    prefix="/ai-roadmap",
    tags=["AI Roadmap"]
)


@router.post(
    "",
    response_model=AIRoadmapResponse
)
def create_ai_roadmap(
    data: AIRoadmapRequest,
    db: Session = Depends(get_db)
):

    roadmap = generate_ai_roadmap(
        db,
        data.student_id,
        data.goal
    )

    return {
        "roadmap": roadmap
    }

