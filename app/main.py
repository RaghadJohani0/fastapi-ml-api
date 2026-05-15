from fastapi import FastAPI
from app.routes.resume import router

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes using AI",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def health():
    return {
        "status": "running",
        "project": "AI Resume Analyzer"
    }
