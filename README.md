<p align="center">
  <img src="banner.png" width="100%">
</p>

# AI Resume Assist

Backend application that analyzes PDF resumes using Google's Gemini AI.

The application extracts text from PDF files, generates structured candidate information, compares resumes against job descriptions and stores the results in PostgreSQL.

This project was built as a way to study AI integration in backend applications using FastAPI, SQLAlchemy and Docker.

---

## Workflow

```text
          Resume.pdf
               │
               ▼
     Text Extraction
        (PyMuPDF)
               │
               ▼
      Google Gemini AI
               │
      ┌────────┴────────┐
      ▼                 ▼
 Resume Analysis   Job Comparison
      │                 │
      └────────┬────────┘
               ▼
         PostgreSQL
               │
               ▼
         JSON Response
```

---

## Features

- Upload PDF resumes
- Extract text using PyMuPDF
- AI-powered resume analysis
- Resume and job description comparison
- PostgreSQL data persistence
- REST API built with FastAPI
- Interactive Swagger documentation

---

## Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend |
| FastAPI | REST API |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Google Gemini | AI Analysis |
| PyMuPDF | PDF Processing |
| Docker | Containerization |
| Docker Compose | Local Environment |

---

## Project Structure

```text
app/
├── models/
├── routes/
├── schemas/
├── services/
├── database.py
├── create_db.py
└── main.py
```
---

## API Endpoints

| Method | Endpoint |
|---------|----------|
| POST | /resume/ |
| GET | /resume/ |
| GET | /resume/{id} |
| PUT | /resume/{id} |
| DELETE | /resume/{id} |
| POST | /resume/upload/{id} |
| POST | /resume/compare/{id} |
| GET | /resume/health |

---

## Running Locally

Clone the repository.

```bash
git clone https://github.com/SEU-USUARIO/AI-RESUME-ASSIST.git
```

Enter the project.

```bash
cd AI-RESUME-ASSIST
```

Create a `.env` file.

```env
GEMINI_API_KEY=your_key

DATABASE_URL=postgresql://postgres:gustavo123@db:5432/airesume
```

Run Docker.

```bash
docker compose up --build
```

Open Swagger.

```
http://localhost:8000/docs
```
---

## Example

### Upload a Resume

```
POST /resume/upload/1
```

↓

Extract PDF

↓

Analyze with Gemini

↓

Store Analysis

↓

Return JSON

---

### Compare Resume

```
POST /resume/compare/1
```

↓

Compare with Job Description

↓

Return Compatibility Report
---

## Future Improvements

- User authentication
- Automated tests
- CI/CD
- Cloud deployment
- Background processing
- Frontend interface
- Resume history
- Better prompt validation
---

## Author

Developed by Gustavo.

Feel free to open an issue or suggest improvements.
