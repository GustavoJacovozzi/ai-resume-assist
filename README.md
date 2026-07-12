<p align="center">
  <img src="banner.png" width="100%">
</p>

# AI Resume Assist

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Ready-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)

Backend application that analyzes PDF resumes using Google Gemini AI.

The application extracts text from PDF files, generates structured candidate information, compares resumes against job descriptions and stores the results in PostgreSQL.

The project was developed as a practical study of AI integration in backend applications using FastAPI, SQLAlchemy and Docker.

---

# Live Demo

### Swagger Documentation

https://ai-resume-assist.onrender.com/docs

---

# Workflow

```text
                 Resume.pdf
                      │
                      ▼
          Text Extraction (PyMuPDF)
                      │
                      ▼
             Google Gemini AI
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
 Resume Analysis          Job Comparison
          │                       │
          └───────────┬───────────┘
                      ▼
                 PostgreSQL
                      │
                      ▼
                JSON Response
```

---

# Features

- Upload PDF resumes
- Extract text using PyMuPDF
- AI-powered resume analysis
- Resume and job description comparison
- Structured JSON responses
- PostgreSQL persistence
- REST API built with FastAPI
- Interactive Swagger documentation
- Docker support

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Google Gemini | AI Processing |
| PyMuPDF | PDF Extraction |
| Docker | Containerization |
| Docker Compose | Local Development |

---

# Project Structure

```text
app/
│
├── models/
├── routes/
├── schemas/
├── services/
│
├── database.py
├── create_db.py
└── main.py

Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /resume/ | Create resume |
| GET | /resume/ | List resumes |
| GET | /resume/{id} | Get resume |
| PUT | /resume/{id} | Update resume |
| DELETE | /resume/{id} | Delete resume |
| POST | /resume/upload/{id} | Upload PDF and analyze |
| POST | /resume/compare/{id} | Compare with job description |
| GET | /resume/health | Health Check |

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/GustavoJacovozzi/ai-resume-assist.git
```

Enter the project

```bash
cd ai-resume-assist
```

Create a `.env`

```env
GEMINI_API_KEY=your_gemini_api_key

DATABASE_URL=postgresql://postgres:gustavo123@db:5432/airesume
```

Start Docker

```bash
docker compose up --build
```

Open Swagger

```
http://localhost:8000/docs
```

---

# Example Flow

### Resume Analysis

```
Upload Resume PDF
        │
        ▼
Extract Text
        │
        ▼
Analyze with Gemini
        │
        ▼
Save Analysis
        │
        ▼
Return JSON
```

---

### Job Comparison

```
Resume
      +
Job Description
        │
        ▼
Google Gemini
        │
        ▼
Compatibility Score
Missing Skills
Strengths
Weaknesses
Suggestions
```

---

# Example Response

```json
{
  "compatibilidade": 87,
  "habilidades_encontradas": [
    "Python",
    "FastAPI",
    "Docker"
  ],
  "habilidades_faltantes": [
    "AWS"
  ],
  "nivel": "Junior",
  "resumo": "The candidate demonstrates good backend development skills with room to improve cloud technologies."
}
```

---

# Future Improvements

- JWT Authentication
- Unit Tests with Pytest
- GitHub Actions CI/CD
- Resume Version History
- Background Tasks
- Rate Limiting
- Frontend Dashboard

---

# Author

**Gustavo Jacobozzi**

Backend Developer

Python • FastAPI • PostgreSQL • Docker • Artificial Intelligence

---

If you have suggestions or find any issues, feel free to open an Issue or submit a Pull Request.
