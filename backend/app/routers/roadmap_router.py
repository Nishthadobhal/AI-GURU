from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.roadmap import (
    RoadmapCreate,
    RoadmapResponse
)

from app.services.roadmap_service import (
    create_roadmap
)


router = APIRouter(
    prefix="/roadmaps",
    tags=["Roadmaps"]
)


@router.post(
    "",
    response_model=RoadmapResponse
)
def add_roadmap(
    roadmap: RoadmapCreate,
    db: Session = Depends(get_db)
):

    return create_roadmap(
        db,
        roadmap
    )