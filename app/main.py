from fastapi import FastAPI
from app.database import Base, engine
from app.models.resume import Resume
from app.routes.resume import router as resume_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(resume_router)