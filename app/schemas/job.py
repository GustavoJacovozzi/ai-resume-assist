from pydantic import BaseModel

class JobDescription(BaseModel):
    descricao: str
    