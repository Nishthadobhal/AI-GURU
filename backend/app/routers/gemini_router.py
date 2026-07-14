from fastapi import APIRouter

from app.schemas.gemini import (
    GeminiRequest,
    GeminiResponse
)

from app.services.gemini_service import (
    ask_gemini
)


router = APIRouter(
    prefix="/gemini",
    tags=["Gemini"]
)


@router.post(
    "",
    response_model=GeminiResponse
)
def chat(
    data: GeminiRequest
):

    answer = ask_gemini(
        data.prompt
    )

    return {
        "response": answer
    }