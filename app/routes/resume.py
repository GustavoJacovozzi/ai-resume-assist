from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate


router = APIRouter(
    prefix="/resume",
    tags= ['Resume']
)

@router.post("/")
def upload_curriculo(
    dados: ResumeCreate,
    db: Session = Depends(get_db)
):
    novo_curriculo = Resume(
        candidate_name = dados.candidate_name,
        email = dados.email,
        skills = dados.skills,
        resume_text= dados.resume_text
    )
    db.add(novo_curriculo)
    db.commit()
    db.refresh(novo_curriculo)
    
    return {
        "id":novo_curriculo.id,
        "mensagem": "Currículo Salvo com sucesso"
    }

@router.get("/")
def listar_curriculo(
    db:Session = Depends(get_db)

):
    return db.query(Resume).all()

@router.get("/{resume_id}")
def buscar_curriculo(
    resume_id: int,
    db:Session = Depends(get_db)


):
    curriculo = (
        db.query(Resume)
        .filter(Resume.id == resume_id)
        .first()
    )
    if curriculo is None:
        raise HTTPException(
            status_code=400,
            detail= "Curriculo Não encontrado!"
        )
    return curriculo

@router.get("/health")
def health_check():
    return {
        "Mensagem": "Vericando API"
    }   
