from pydantic import BaseModel
class ResumeCreate(BaseModel):
    candidate_name: str
    email: str
    skills:str
    resume_text:str

class ResumeResponse(BaseModel):
    id: int
    candidate_name: str
    email:str
    skills: str
    resume_text:str

    class config:
        from_attributes = True

class ResumeUpdate(BaseModel):
    candidata_name: str
    email: str
    skills: str
    resume_text: str
    
