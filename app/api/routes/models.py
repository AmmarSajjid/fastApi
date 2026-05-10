from fastapi import APIRouter

router = APIRouter(tags=["models"])



@router.get("/v1/models")
def get_models() -> dict:
    return {"models": ["gpt", "claude", "gemini"]}

