def get_career_recommendation(profile):
    skills = set(map(str.lower, profile.get("skills", [])))
    interests = set(map(str.lower, profile.get("interests", [])))
    strengths = set(map(str.lower, profile.get("strengths", [])))

    # === Tech Careers ===
    if "machine learning" in skills or "ai" in interests:
        return (
            "🎯 Career: Machine Learning Engineer / AI Researcher\n"
            "🔧 Skills: Python, TensorFlow, PyTorch, Data Science, Cloud Platforms"
        )
    elif "web development" in skills or "frontend" in interests:
        return (
            "🎯 Career: Front-End Developer / UI Developer\n"
            "🔧 Skills: HTML, CSS, JavaScript, React, UX Design"
        )
    elif "backend" in skills or "api" in interests:
        return (
            "🎯 Career: Back-End Developer / API Engineer\n"
            "🔧 Skills: Node.js, Django, REST APIs, Databases, Authentication"
        )
    elif "mobile development" in skills:
        return (
            "🎯 Career: Mobile App Developer\n"
            "🔧 Skills: Flutter, Swift, Kotlin, Firebase, UI/UX Design"
        )
    elif "cybersecurity" in interests or "networking" in skills:
        return (
            "🎯 Career: Cybersecurity Analyst / Ethical Hacker\n"
            "🔧 Skills: Network Security, Linux, Kali Linux, Wireshark, Pen Testing"
        )
    elif "data" in interests or "data analysis" in skills:
        return (
            "🎯 Career: Data Analyst / Data Scientist\n"
            "🔧 Skills: SQL, Python (Pandas, NumPy), Data Visualization, BI Tools"
        )
    elif "cloud" in skills or "devops" in interests:
        return (
            "🎯 Career: DevOps Engineer / Cloud Engineer\n"
            "🔧 Skills: Docker, Kubernetes, CI/CD, AWS, Terraform"
        )
    elif "game development" in interests:
        return (
            "🎯 Career: Game Developer\n"
            "🔧 Skills: Unity, C#, Unreal Engine, 3D Modeling, Game Design"
        )

    # === Non-Tech Careers ===
    elif "finance" in interests or "economics" in strengths:
        return (
            "🎯 Career: Financial Analyst / Investment Banker\n"
            "🔧 Skills: Excel, Financial Modeling, Accounting, Bloomberg, CFA Basics"
        )
    elif "graphic design" in interests or "creativity" in strengths:
        return (
            "🎯 Career: Graphic Designer / UI Designer\n"
            "🔧 Skills: Photoshop, Illustrator, Figma, Typography, Branding"
        )
    elif "writing" in strengths or "communication" in interests:
        return (
            "🎯 Career: Content Writer / Copywriter / Journalist\n"
            "🔧 Skills: SEO, Research, Writing Tools, WordPress, Editorial Skills"
        )
    elif "marketing" in interests or "social media" in skills:
        return (
            "🎯 Career: Digital Marketing Specialist\n"
            "🔧 Skills: SEO, SEM, Google Ads, Analytics, Social Media Strategy"
        )
    elif "teaching" in strengths or "education" in interests:
        return (
            "🎯 Career: Educator / Instructional Designer\n"
            "🔧 Skills: LMS Tools, Pedagogy, Subject Expertise, Communication"
        )
    elif "law" in interests or "debate" in strengths:
        return (
            "🎯 Career: Lawyer / Legal Analyst\n"
            "🔧 Skills: Legal Research, Argumentation, Documentation, Case Law"
        )
    elif "biology" in interests or "medicine" in strengths:
        return (
            "🎯 Career: Healthcare Professional / Medical Researcher\n"
            "🔧 Skills: Biology, Chemistry, Human Anatomy, Medical Aptitude"
        )
    elif "entrepreneurship" in interests or "leadership" in strengths:
        return (
            "🎯 Career: Entrepreneur / Startup Founder\n"
            "🔧 Skills: Business Planning, Marketing, Fundraising, Product Development"
        )

    # === Default Recommendation ===
    else:
        return (
            "🎯 Career: Software Developer / Tech Generalist\n"
            "🔧 Skills: Problem Solving, Programming (C++/Java/Python), DSA, Git, Agile"
        )
