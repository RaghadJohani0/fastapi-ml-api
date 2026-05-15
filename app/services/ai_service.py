def analyze_resume(text):

    skills = []

    if "python" in text.lower():
        skills.append("Python")

    if "fastapi" in text.lower():
        skills.append("FastAPI")

    if "docker" in text.lower():
        skills.append("Docker")


    score = len(skills) * 25

    return {

        "skills": skills,

        "score": score,

        "recommendation":
        "Add more backend projects"

    }
