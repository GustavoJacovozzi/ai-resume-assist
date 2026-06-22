from fastapi import FastAPI
from app.routes.resume import router as resume_router

app = FastAPI(
    title = "AI Resume Assist",
    version = "1.0"
)
app.include_router(resume_router)
