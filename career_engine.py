career_info = {

    "Doctor": {
        "powers": ["Biology", "Empathy", "Critical Thinking", "Communication"],
        "mission": "Volunteer at a hospital or complete an online anatomy course.",
        "journey": "Medical School → Residency → Doctor",
        "obstacle": "Long years of study and high responsibility."
    },

    "Surgeon": {
        "powers": ["Precision", "Biology", "Decision Making", "Calm Under Pressure"],
        "mission": "Study anatomy and practice fine motor skills.",
        "journey": "Medical School → Surgical Residency",
        "obstacle": "Demanding training and long hours."
    },

    "Nurse": {
        "powers": ["Compassion", "Communication", "Patient Care", "Teamwork"],
        "mission": "Volunteer in healthcare or first aid programs.",
        "journey": "Nursing Degree → Registered Nurse",
        "obstacle": "Long shifts."
    },

    "Psychologist": {
        "powers": ["Empathy", "Listening", "Research", "Communication"],
        "mission": "Read introductory psychology books.",
        "journey": "Psychology Degree → Psychologist",
        "obstacle": "Emotionally challenging work."
    },

    "Software Engineer": {
        "powers": ["Python", "Programming", "Problem Solving", "Logic"],
        "mission": "Build your first website or app.",
        "journey": "Computer Science → Software Engineer",
        "obstacle": "Technology changes quickly."
    },

    "AI Engineer": {
        "powers": ["Machine Learning", "Python", "Mathematics", "Problem Solving"],
        "mission": "Create an AI chatbot.",
        "journey": "Computer Science → AI Engineer",
        "obstacle": "Continuous learning."
    },

    "Cybersecurity Analyst": {
        "powers": ["Networking", "Linux", "Security", "Analytical Thinking"],
        "mission": "Complete beginner cybersecurity labs.",
        "journey": "IT Degree → Cybersecurity",
        "obstacle": "Cyber threats evolve constantly."
    },

    "Data Scientist": {
        "powers": ["Statistics", "Python", "Data Analysis", "Machine Learning"],
        "mission": "Analyze a real-world dataset.",
        "journey": "Data Science → Data Scientist",
        "obstacle": "Complex data."
    },

    "Biomedical Engineer": {
        "powers": ["Biology", "Engineering", "Innovation", "Problem Solving"],
        "mission": "Build a simple health-tech project.",
        "journey": "Biomedical Engineering Degree",
        "obstacle": "Combining medicine and engineering."
    },

    "Lawyer": {
        "powers": ["Research", "Communication", "Debating", "Critical Thinking"],
        "mission": "Join a debate competition.",
        "journey": "Law School → Lawyer",
        "obstacle": "Highly competitive field."
    },

    "Teacher": {
        "powers": ["Communication", "Patience", "Leadership", "Organization"],
        "mission": "Tutor another student.",
        "journey": "Education Degree → Teacher",
        "obstacle": "Managing different learning styles."
    },

    "Business Entrepreneur": {
        "powers": ["Leadership", "Marketing", "Finance", "Decision Making"],
        "mission": "Start a small online business.",
        "journey": "Business Studies → Entrepreneur",
        "obstacle": "Financial risk."
    },

    "Marketing Manager": {
        "powers": ["Creativity", "Communication", "Marketing", "Analytics"],
        "mission": "Create a marketing campaign.",
        "journey": "Marketing Degree → Marketing Manager",
        "obstacle": "Keeping up with trends."
    },

    "Accountant": {
        "powers": ["Mathematics", "Accuracy", "Finance", "Organization"],
        "mission": "Learn Excel and accounting basics.",
        "journey": "Accounting Degree → Accountant",
        "obstacle": "Attention to detail."
    },

    "Architect": {
        "powers": ["Design", "Creativity", "Mathematics", "Visualization"],
        "mission": "Design your dream home.",
        "journey": "Architecture Degree → Architect",
        "obstacle": "Balancing creativity and engineering."
    },

    "Civil Engineer": {
        "powers": ["Physics", "Mathematics", "Planning", "Problem Solving"],
        "mission": "Learn CAD software.",
        "journey": "Civil Engineering Degree",
        "obstacle": "Large project responsibility."
    },

    "Graphic Designer": {
        "powers": ["Creativity", "Typography", "Photoshop", "Communication"],
        "mission": "Design a logo.",
        "journey": "Design Degree → Graphic Designer",
        "obstacle": "Client expectations."
    },

    "UX Designer": {
        "powers": ["User Research", "Creativity", "Figma", "Problem Solving"],
        "mission": "Design a mobile app interface.",
        "journey": "UX Design → UX Designer",
        "obstacle": "Balancing user and business needs."
    },

    "Pilot": {
        "powers": ["Focus", "Decision Making", "Mathematics", "Calmness"],
        "mission": "Practice with flight simulators.",
        "journey": "Flight School → Airline Pilot",
        "obstacle": "Strict training."
    },

    "Scientist": {
        "powers": ["Research", "Critical Thinking", "Curiosity", "Analysis"],
        "mission": "Conduct a simple science project.",
        "journey": "Science Degree → Research Scientist",
        "obstacle": "Years of research."
    },
        "Pharmacist": {
        "powers": [
            "Chemistry",
            "Attention to Detail",
            "Medicine Knowledge",
            "Communication"
        ],
        "mission": "Learn the basics of medicines and complete an introductory pharmacology course.",
        "journey": "Pharmacy Degree → Licensed Pharmacist",
        "obstacle": "Keeping up with new medications and ensuring prescriptions are accurate."
    }
}


def recommend_careers(subjects, interests, strengths):

    text = (" ".join(subjects) + " " + interests + " " + strengths).lower()

    careers = {career: 0 for career in career_info.keys()}

    # Medicine
    if "biology" in text:
        careers["Doctor"] += 40
        careers["Surgeon"] += 35
        careers["Biomedical Engineer"] += 25

    if "chemistry" in text:
        careers["Doctor"] += 20
        careers["Pharmacist"] = careers.get("Pharmacist", 0) + 35

    if "help" in text or "people" in text:
        careers["Doctor"] += 20
        careers["Nurse"] += 30
        careers["Psychologist"] += 30
        careers["Teacher"] += 20

    # Computing
    if "computer science" in text:
        careers["Software Engineer"] += 40
        careers["AI Engineer"] += 35
        careers["Cybersecurity Analyst"] += 25

    if "coding" in text or "programming" in text:
        careers["Software Engineer"] += 40
        careers["AI Engineer"] += 30

    if "ai" in text or "artificial intelligence" in text:
        careers["AI Engineer"] += 50

    # Maths
    if "mathematics" in text:
        careers["Data Scientist"] += 30
        careers["Civil Engineer"] += 20
        careers["Accountant"] += 20

    if "physics" in text:
        careers["Civil Engineer"] += 30
        careers["Scientist"] += 20
        careers["Pilot"] += 20

    # Business
    if "business" in text:
        careers["Business Entrepreneur"] += 40
        careers["Marketing Manager"] += 30

    if "economics" in text:
        careers["Business Entrepreneur"] += 20
        careers["Accountant"] += 30

    if "leadership" in text:
        careers["Business Entrepreneur"] += 30

    # Law
    if "english" in text:
        careers["Lawyer"] += 20

    if "debate" in text:
        careers["Lawyer"] += 40

    # Design
    if "art" in text:
        careers["Graphic Designer"] += 30
        careers["UX Designer"] += 25
        careers["Architect"] += 20

    if "creative" in text:
        careers["Graphic Designer"] += 25
        careers["UX Designer"] += 25

    if "design" in text:
        careers["Graphic Designer"] += 30
        careers["Architect"] += 20
        careers["UX Designer"] += 30

    ranked = sorted(careers.items(), key=lambda x: x[1], reverse=True)

    return ranked[:3], career_info
