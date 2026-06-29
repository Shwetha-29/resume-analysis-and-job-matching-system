from flask import Flask, render_template, request, send_file

from models.parser import extract_text_from_pdf, clean_text
from models.analyzer import extract_keywords, compare_keywords
from models.report_generator import generate_report
from models.dashboard import generate_dashboard
from models.section_analyzer import analyze_sections
from models.ats_score import calculate_weighted_score
from models.role_predictor import predict_roles
from models.ai_insights import generate_ai_insights
from models.recruiter_summary import generate_recruiter_summary
from models.resume_health import get_resume_health
from models.progress_color import get_progress_color
from models.score_level import get_score_level

app = Flask(__name__)

latest_report = {}

SECTION_HEADINGS = (
    "EDUCATION",
    "SKILLS",
    "PROJECTS",
    "EXPERIENCE",
    "CERTIFICATION",
    "CERTIFICATIONS",
    "LANGUAGES",
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    global latest_report

    resume_file = request.files["resume"]
    job_description = request.form["job_description"]

    # ------------------------------------------------
    # Extract Resume Text
    # ------------------------------------------------
    resume_text = extract_text_from_pdf(resume_file)

    # ------------------------------------------------
    # Normalize Section Headings
    # ------------------------------------------------
    for heading in SECTION_HEADINGS:
        resume_text = resume_text.replace(
            heading,
            f"\n{heading}\n"
        )

    # ------------------------------------------------
    # Debug Resume Text
    # ------------------------------------------------
    print("\n========== RESUME TEXT ==========\n")
    print(resume_text)
    print("\n========== END ==========\n")

    # ------------------------------------------------
    # Resume Sections
    # ------------------------------------------------
    sections = analyze_sections(resume_text)

    # ------------------------------------------------
    # Clean Text
    # ------------------------------------------------
    resume_tokens = clean_text(resume_text)
    job_tokens = clean_text(job_description)

    # ------------------------------------------------
    # Extract Skills
    # ------------------------------------------------
    resume_keywords = extract_keywords(resume_tokens)
    job_keywords = extract_keywords(job_tokens)

    # ------------------------------------------------
    # Compare Skills
    # ------------------------------------------------
    found, missing, skill_score = compare_keywords(
        resume_keywords,
        job_keywords
    )

    print(job_keywords)
    
    # ------------------------------------------------
    # ATS Score
    # ------------------------------------------------
    score, score_breakdown = calculate_weighted_score(
        skill_score,
        sections
    )

    score_color = get_progress_color(score)
    score_level = get_score_level(score)

    score_breakdown_colors = {
        section: get_progress_color(value)
        for section, value in score_breakdown.items()
    }

    # ------------------------------------------------
    # Skill Dashboard
    # ------------------------------------------------
    dashboard = generate_dashboard(
        resume_keywords,
        job_keywords
    )

    for data in dashboard.values():
        data["color"] = get_progress_color(
            data["percentage"]
        )

    # ------------------------------------------------
    # Career Role Prediction
    # ------------------------------------------------
    predictions = predict_roles(
        resume_keywords,
        job_keywords,
        sections
    )

    print(predictions)

    for role in predictions:
        role["color"] = get_progress_color(
            role["score"]
        )

    # ------------------------------------------------
    # AI Resume Insights
    # ------------------------------------------------
    insights = generate_ai_insights(
        resume_keywords=resume_keywords,
        missing_skills=missing,
        sections=sections,
        predictions=predictions,
        score=score
    )

    recruiter_summary = generate_recruiter_summary(
        predictions,
        insights
    )

    resume_health = get_resume_health(score)

    # ------------------------------------------------
    # Statistics
    # ------------------------------------------------
    stats = {
        "total": len(job_keywords),
        "found": len(found),
        "missing": len(missing)
    }

    # ------------------------------------------------
    # Suggestions
    # ------------------------------------------------
    suggestions = [
        f"Consider adding '{skill.title()}' to your resume if you have relevant experience."
        for skill in sorted(missing)
    ]

    if not suggestions:
        suggestions.append(
            "Excellent! Your resume contains all the required technical skills."
        )

    # ------------------------------------------------
    # Store Report Data
    # ------------------------------------------------
    latest_report = {
        "score": score,
        "job_keywords": job_keywords,
        "resume_keywords": resume_keywords,
        "found": found,
        "missing": missing,
        "suggestions": suggestions
    }

    # ------------------------------------------------
    # Render Template
    # ------------------------------------------------
    return render_template(
        "index.html",
        score=score,
        score_breakdown=score_breakdown,
        stats=stats,
        dashboard=dashboard,
        sections=sections,
        found=sorted(found),
        missing=sorted(missing),
        job_keywords=sorted(job_keywords),
        resume_keywords=sorted(resume_keywords),
        suggestions=suggestions,
        predictions=predictions,
        insights=insights,
        recruiter_summary=recruiter_summary,
        resume_health=resume_health,
        score_color=score_color,
        score_breakdown_colors=score_breakdown_colors,
        score_level=score_level
    )


@app.route("/download-report")
def download_report():

    if not latest_report:
        return "Analyze a resume first."

    filename = "Resume_Analysis_Report.pdf"

    generate_report(
        filename,
        latest_report["score"],
        latest_report["job_keywords"],
        latest_report["resume_keywords"],
        latest_report["found"],
        latest_report["missing"],
        latest_report["suggestions"]
    )

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)