# Resume Analysis and Job Matching System

An AI-powered web application that analyzes resumes against job descriptions to evaluate ATS (Applicant Tracking System) compatibility. The system extracts technical skills, identifies missing keywords, predicts suitable career roles, provides recruiter-style insights, and generates a detailed PDF report.

---

## Features

- 📄 Upload resumes in PDF format
- 📝 Analyze resumes against any job description
- 📊 Calculate ATS Match Score
- ✅ Detect matched and missing skills
- 📈 Skill Gap Dashboard
- 👨‍💼 AI Recruiter Summary
- 🧠 AI Resume Insights
- 🎯 Career Role Prediction
- 📑 Resume Section Analysis
- ❤️ Resume Health Assessment
- 📥 Download Detailed PDF Report

---

## Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- PyMuPDF (fitz)
- ReportLab
- NLTK
- Regular Expressions

---

## Project Structure

```
Resume-Analysis-and-Job-Matching-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── skills.json
│
├── models/
│   ├── analyzer.py
│   ├── ats_score.py
│   ├── ai_insights.py
│   ├── dashboard.py
│   ├── parser.py
│   ├── progress_color.py
│   ├── recruiter_summary.py
│   ├── report_generator.py
│   ├── resume_health.py
│   ├── role_predictor.py
│   ├── section_analyzer.py
│   ├── score_level.py
│   ├── skill_formatter.py
│   └── ...
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
└── reports/
```

---

## How It Works

1. Upload a resume in PDF format.
2. Paste the target job description.
3. The system extracts text from the resume.
4. Technical skills are identified using NLP-based keyword extraction.
5. Resume skills are compared with the job description.
6. ATS Match Score is calculated.
7. Suitable career roles are predicted.
8. AI-generated recruiter insights and recommendations are displayed.
9. A detailed PDF report can be downloaded.

---

## ATS Analysis Includes

- ATS Match Score
- Technical Skill Analysis
- Resume Health
- Resume Section Analysis
- Skill Gap Dashboard
- AI Resume Insights
- Recruiter Summary
- Career Role Prediction
- Suggestions for Missing Skills
- PDF Report Generation

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shwetha-29/resume-analysis-and-job-matching-system.git
```

### 2. Navigate to the project

```bash
cd resume-analysis-and-job-matching-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

---

## Example Workflow

- Upload Resume
- Enter Job Description
- View ATS Match Score
- Review Missing Skills
- Check Career Role Predictions
- Read AI Recruiter Feedback
- Download PDF Report

---

## Future Enhancements

- Support DOCX resumes
- Semantic skill matching using embeddings
- Resume improvement suggestions using LLMs
- Multiple resume comparison
- Company-specific ATS optimization
- Authentication and user accounts
- Resume history dashboard
