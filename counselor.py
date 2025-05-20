def get_career_recommendation(profile):
    skills = set(map(str.lower, profile.get("skills", [])))
    interests = set(map(str.lower, profile.get("interests", [])))
    strengths = set(map(str.lower, profile.get("strengths", [])))

    # Rule-based logic for career suggestions
    if "machine learning" in skills or "ai" in interests:
        return (
            "🎯 Suggested Career Path: Machine Learning Engineer / AI Specialist\n"
            "🔧 Recommended Skills:\n"
            "- Python\n"
            "- scikit-learn, TensorFlow, PyTorch\n"
            "- Data Preprocessing\n"
            "- Linear Algebra & Statistics\n"
            "- Model Deployment (Flask, FastAPI)\n"
            "- Cloud Platforms (AWS/GCP)"
        )
    elif "web development" in skills or "frontend" in interests or "backend" in interests:
        return (
            "🎯 Suggested Career Path: Full-Stack Web Developer\n"
            "🔧 Recommended Skills:\n"
            "- HTML, CSS, JavaScript\n"
            "- React / Angular (Frontend)\n"
            "- Node.js / Django / Flask (Backend)\n"
            "- REST APIs, Authentication\n"
            "- Git & GitHub\n"
            "- Deployment (Netlify, Vercel, Render)"
        )
    elif "data analysis" in skills or "data" in interests:
        return (
            "🎯 Suggested Career Path: Data Analyst / Data Scientist\n"
            "🔧 Recommended Skills:\n"
            "- Excel, SQL\n"
            "- Python (Pandas, NumPy, Matplotlib)\n"
            "- Power BI / Tableau\n"
            "- Data Cleaning & Visualization\n"
            "- Statistical Analysis\n"
            "- Reporting & Dashboards"
        )
    elif "communication" in strengths or "management" in interests:
        return (
            "🎯 Suggested Career Path: Business Analyst / Product Manager\n"
            "🔧 Recommended Skills:\n"
            "- Requirement Gathering\n"
            "- Stakeholder Communication\n"
            "- Agile / Scrum Methodologies\n"
            "- JIRA / Confluence\n"
            "- Data-Driven Decision Making\n"
            "- Basic SQL & Dashboards"
        )
    elif "cybersecurity" in interests or "networking" in skills:
        return (
            "🎯 Suggested Career Path: Cybersecurity Analyst / Ethical Hacker\n"
            "🔧 Recommended Skills:\n"
            "- Network Fundamentals\n"
            "- Linux & Shell Scripting\n"
            "- Firewalls, IDS/IPS\n"
            "- Security Tools (Wireshark, Nmap, Metasploit)\n"
            "- Ethical Hacking Basics\n"
            "- Security Certifications (CEH, CompTIA Security+)"
        )
    elif "mobile development" in skills:
        return (
            "🎯 Suggested Career Path: Mobile App Developer\n"
            "🔧 Recommended Skills:\n"
            "- Java / Kotlin (Android)\n"
            "- Swift (iOS)\n"
            "- Flutter / React Native (Cross-platform)\n"
            "- UI/UX Design Principles\n"
            "- Firebase Integration\n"
            "- App Store Deployment"
        )
    else:
        return (
            "🎯 Suggested Career Path: Software Developer / Generalist\n"
            "🔧 Recommended Skills:\n"
            "- Data Structures & Algorithms\n"
            "- Problem Solving (LeetCode / HackerRank)\n"
            "- One Backend Language (Python/Java/C++)\n"
            "- Version Control (Git)\n"
            "- Debugging & Testing\n"
            "- System Design Basics"
        )
