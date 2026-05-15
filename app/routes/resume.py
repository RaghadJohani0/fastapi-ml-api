from fastapi import APIRouter, UploadFile, File
from app.services.ai_service import analyze_resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(
        file: UploadFile = File(...)
):

    content = await file.read()

    text = content.decode(
        errors="ignore"
    )

    result = analyze_resume(text)

    return result
