def recommend_careers(subjects, interests, strengths):

    text = (" ".join(subjects) + " " + interests + " " + strengths).lower()

    careers = {
        "Doctor": 0,
        "AI Engineer": 0,
        "Entrepreneur": 0,
        "Lawyer": 0,
        "UX Designer": 0,
        "Biomedical Engineer": 0,
        "Psychologist": 0,
        "Data Scientist": 0
    }

    # Doctor
    if "biology" in text:
        careers["Doctor"] += 30
    if "chemistry" in text:
        careers["Doctor"] += 20
    if "help" in text or "people" in text:
        careers["Doctor"] += 20

    # AI Engineer
    if "computer science" in text:
        careers["AI Engineer"] += 30
    if "coding" in text or "programming" in text:
        careers["AI Engineer"] += 30
    if "technology" in text or "ai" in text:
        careers["AI Engineer"] += 20

    # Entrepreneur
    if "business" in text:
        careers["Entrepreneur"] += 30
    if "economics" in text:
        careers["Entrepreneur"] += 20
    if "leadership" in text:
        careers["Entrepreneur"] += 20

    # Lawyer
    if "english" in text:
        careers["Lawyer"] += 20
    if "debate" in text:
        careers["Lawyer"] += 30

    # UX Designer
    if "art" in text:
        careers["UX Designer"] += 30
    if "creative" in text:
        careers["UX Designer"] += 25
    if "design" in text:
        careers["UX Designer"] += 20

    # Biomedical Engineer
    if "biology" in text and "technology" in text:
        careers["Biomedical Engineer"] += 40

    # Psychologist
    if "help" in text:
        careers["Psychologist"] += 20
    if "people" in text:
        careers["Psychologist"] += 20

    # Data Scientist
    if "mathematics" in text:
        careers["Data Scientist"] += 30
    if "physics" in text:
        careers["Data Scientist"] += 20

    ranked = sorted(careers.items(), key=lambda x: x[1], reverse=True)

    return ranked[:3]
