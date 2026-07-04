from sqlalchemy import Column, Integer, Text, String
from app.database import Base

class Resume(Base):
    __tablename__ = "resumes"
 
    id = Column(Integer,primary_key=True,index=True)
    candidate_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    skills = Column(Text)
    resume_text = Column(Text)

    analysis_name = Column(String)
    analysis_skills = Column(String)
    analysis_experience = Column(Integer)
    analysis_level = Column(Text)
    analysis_summary = Column(Text)



 