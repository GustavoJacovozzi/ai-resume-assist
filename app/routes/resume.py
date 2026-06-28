from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate, ResumeUpdate
import fitz

router = APIRouter(
    prefix="/resume",
    tags= ['Resume']
)

@router.post("/")
def criar_curriculo(
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

@router.delete("/{resume_id}")
def deletar_curriculo(
    resume_id: int,
    db: Session = Depends(get_db)

):
    curriculo = (
        db.query(Resume)
        .filter(resume_id==resume_id)
        .first()

    )

    if curriculo is None:
        raise HTTPException(
            status_code= 404,
            detail= "Curriculo Não encontrado"

        )
    db.delete(curriculo)
    db.commit()
    return{
        "Mensagem": "Curriculo Removido com Sucesso"
    }

@router.put("/{resume_id}")
def atualizar_curriculo(
    resume_id: int,
    dados: ResumeUpdate,
    db:Session = Depends(get_db)
):
    curriculo = (
        db.query(Resume)
        .filter(Resume.id==resume_id)
        .first()
    )
    if curriculo is None:
        raise HTTPException(
            status_code=404,
            detail= "Curriculo Não encontrado"

        )
    curriculo.candidate_name = dados.candidate_name
    curriculo.email = dados.email
    curriculo.skills = dados.skills
    curriculo.resume_text = dados.resume_text
    db.commit()
    db.refresh()
    return{
        "Mensagem": "Curriculo Atualizado com sucesso",
        "Curriculo": curriculo
    }
           
@router.post("/upload")
async def upload_curriculo(
    arquivo: UploadFile = File(...)

):
    pdf_byte = await arquivo.read()
    pdf = fitz.open(stream=pdf_byte, filetype="pdf")
    texto = ""
    for pagina in pdf:
        texto += pagina.get_text()
    return{
        "nome": arquivo.filename,
        "texto": texto
    }   