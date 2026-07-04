import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analisar_curriculo(texto: str) -> dict:
    prompt = f"""
Você é um especialista em RH.

Analise o currículo abaixo.

Retorne APENAS um JSON.

Formato:

{{
    "nome":"",
    "hard_skills":[],
    "soft_skills":[],
    "tecnologias":[],
    "idiomas":[],
    "certificacoes":[],
    "experiencia_anos":0,
    "nivel":"",
    "resumo":""
}}

Currículo:

{texto}
"""


    resposta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(resposta.text)

    texto_json = resposta.text.strip()

    if texto_json.startswith("```json"):
        texto_json = texto_json[7:]

    if texto_json.endswith("```"):
        texto_json = texto_json[:-3]

    texto_json = texto_json.strip()

    return json.loads(texto_json)
def comparar_vaga(curriculo: str, vaga: str) -> dict:
    prompt = f"""
Você é um recrutador especialista em tecnologia.

Compare o currículo com a vaga e responda APENAS um JSON.

Formato:

{{
    "compatibilidade": 0,
    "habilidades_encontradas": [],
    "habilidades_faltantes": [],
    "pontos_fortes": [],
    "pontos_fracos": [],
    "sugestoes": [],
    "resumo": ""
}}

Currículo:

{curriculo}

Descrição da vaga:

{vaga}
"""

    resposta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print(resposta.text)

    texto = resposta.text.strip()

    if texto.startswith("```json"):
        texto = texto[7:]

    if texto.endswith("```"):
        texto = texto[:-3]

    texto = texto.strip()

    return json.loads(texto)