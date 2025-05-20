def get_career_recommendation(profile):
    skills = set(map(str.lower, profile.get("skills", [])))
    interests = set(map(str.lower, profile.get("interests", [])))

    if "machine learning" in skills or "ai" in interests:
        return "Suggested Career Path: Machine Learning Engineer or Data Scientist.\nRecommended Skills to Build: Deep Learning, Python Libraries (e.g., NumPy, Pandas, scikit-learn)."
    elif "web development" in skills:
        return "Suggested Career Path: Full-Stack Web Developer.\nRecommended Skills to Build: JavaScript, React, Backend APIs."
    elif "communication" in interests or "management" in interests:
        return "Suggested Career Path: Business Analyst or Product Manager.\nRecommended Skills to Build: Agile Methodology, Data Visualization, Stakeholder Communication."
    else:
        return "Suggested Career Path: Software Developer.\nRecommended Skills to Build: Data Structures, Algorithms, System Design."
