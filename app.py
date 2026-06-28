import streamlit as st
from career_engine import recommend_careers

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="FutureMirror AI",
    page_icon="🪞",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🪞 FutureMirror AI")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🪞 Discover My Future",
        "📚 Career Library",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "🏠 Home":

    st.markdown("""
    <style>
    .hero{
        background: linear-gradient(135deg,#4F46E5,#7C3AED);
        padding:45px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    }

    .hero h1{
        font-size:55px;
        margin-bottom:10px;
    }

    .hero h3{
        font-weight:400;
        color:#E5E7EB;
    }

.card{
    background:#f8f9fa;
    color:#111827;
    padding:25px;
    border-radius:15px;
    border-left:6px solid #7C3AED;
    margin-top:20px;
}
    .quote{
        text-align:center;
        font-size:22px;
        font-style:italic;
        margin-top:30px;
        color:#555;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">

    <h1>🪞 FutureMirror AI</h1>

    <h3>Who could you become tomorrow?</h3>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🌍 Why FutureMirror AI?

    Choosing a career is one of the biggest decisions a student will ever make.

    Unfortunately, many students don't know where to begin.

    **FutureMirror AI helps students explore personalized career paths based on their interests, strengths, personality and ambitions.**
    """)

    st.markdown("""
    <div class="card">

    ## 🚀 What you'll receive

    ✅ Three personalized future career paths

    ✅ Skills you should learn

    ✅ University & education suggestions

    ✅ Real projects to build

    ✅ Your first mission to get started

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quote">

    "The future isn't something you find.

    It's something you build."

    </div>
    """, unsafe_allow_html=True)

    st.success("👉 Click **🪞 Discover My Future** from the sidebar to begin.")

# -----------------------------
# DISCOVER PAGE
# -----------------------------
elif page == "🪞 Discover My Future":

    import time

    st.title("🪞 Discover My Future")

    st.markdown(
        "Answer a few questions and let FutureMirror AI explore three possible futures for you."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")

        age = st.slider("Age",13,25,16)

        grade = st.selectbox(
            "Current Grade",
            [
                "Grade 8",
                "Grade 9",
                "Grade 10",
                "Grade 11",
                "Grade 12",
                "University"
            ]
        )

        subjects = st.multiselect(
            "Favorite Subjects",
            [
                "Mathematics",
                "Physics",
                "Computer Science",
                "Biology",
                "Chemistry",
                "Business",
                "Economics",
                "English",
                "Art"
            ]
        )

    with col2:

        interests = st.text_area(
            "What are your biggest interests?",
            placeholder="Gaming, coding, football, business, helping people..."
        )

        strengths = st.text_area(
            "What are your biggest strengths?",
            placeholder="Creative, leadership, problem solving..."
        )

        goals = st.text_area(
            "What impact do you want to make?",
            placeholder="Build technology, help people, solve climate change..."
        )

    st.divider()

    if st.button("🪞 Reveal My Futures",use_container_width=True):

        progress = st.progress(0)

        status = st.empty()

        status.write("🪞 Initializing Mirror...")
        progress.progress(20)
        time.sleep(1)

        status.write("🧠 Analyzing strengths...")
        progress.progress(45)
        time.sleep(1)

        status.write("📚 Matching careers...")
        progress.progress(70)
        time.sleep(1)

        status.write("✨ Building future reflections...")
        progress.progress(100)
        time.sleep(1)

        status.success("Mirror Unlocked!")
        top_careers, career_info = recommend_careers(subjects, interests, strengths)

        st.balloons()

        st.divider()

        with st.expander("🟢 Reflection Alpha",expanded=True):

            career, score = top_careers[0]
            info = career_info[career]

            st.subheader(career)

            st.metric("Compatibility", f"{min(score + 40, 99)}%")

            st.markdown("### 💬 Future Snapshot")

            st.info(f"Imagine yourself a few years from now working as a **{career}**, using your skills to make a real impact every day.")

            st.markdown("### 🧠 Powers You'll Need")

            for power in info["powers"]:
                st.write(f"- {power}")

            st.markdown("### 🚀 First Mission")

            st.success(info["mission"])

            st.markdown("### 🎓 Journey Ahead")

            st.write(info["journey"])

            st.markdown("### ⚠ Biggest Obstacle")

            st.warning(info["obstacle"])
        with st.expander("🟣 Reflection Beta"):

            career, score = top_careers[1]
            info = career_info[career]

            st.subheader(career)

            st.metric("Compatibility", f"{min(score + 40, 99)}%")

            st.info(f"Imagine yourself a few years from now working as a **{career}**, using your skills to make a real impact every day.")

            for power in info["powers"]:
               st.write(f"- {power}")

            st.success(info["mission"])

            st.write(info["journey"])

            st.warning(info["obstacle"])

        with st.expander("🔵 Reflection Gamma"):

            career, score = top_careers[2]
            info = career_info[career]

            st.subheader(career)

            st.metric("Compatibility", f"{min(score + 40, 99)}%")

            st.info(f"Imagine yourself a few years from now working as a **{career}**, using your skills to make a real impact every day.")

            for power in info["powers"]:
              st.write(f"- {power}")

            st.success(info["mission"])

            st.write(info["journey"])

            st.warning(info["obstacle"])

# -----------------------------
# CAREER LIBRARY
# -----------------------------
elif page == "📚 Career Library":

    st.title("📚 Career Library")

    careers = [
        {
            "name": "👨‍⚕️ Doctor",
            "description": "Diagnoses illnesses and helps patients recover.",
            "salary": "$80k–250k/year",
            "skills": "Biology, Communication, Empathy",
            "degree": "Medicine (MBBS/MD)"
        },
        {
            "name": "🤖 AI Engineer",
            "description": "Builds intelligent software and machine learning systems.",
            "salary": "$90k–180k/year",
            "skills": "Python, AI, Problem Solving",
            "degree": "Computer Science"
        },
        {
            "name": "💼 Entrepreneur",
            "description": "Starts and grows businesses to solve problems.",
            "salary": "Varies",
            "skills": "Leadership, Business, Creativity",
            "degree": "Business (optional)"
        },
        {
            "name": "⚖️ Lawyer",
            "description": "Represents clients and provides legal advice.",
            "salary": "$70k–180k/year",
            "skills": "Communication, Research, Critical Thinking",
            "degree": "Law"
        },
        {
            "name": "🎨 UX Designer",
            "description": "Designs websites and apps that people enjoy using.",
            "salary": "$70k–140k/year",
            "skills": "Creativity, Design, User Research",
            "degree": "Design or Computer Science"
        },
        {
            "name": "🧠 Psychologist",
            "description": "Helps people improve their mental health.",
            "salary": "$60k–130k/year",
            "skills": "Listening, Empathy, Analysis",
            "degree": "Psychology"
        },
        {
            "name": "🧬 Biomedical Engineer",
            "description": "Creates medical technology and healthcare devices.",
            "salary": "$80k–150k/year",
            "skills": "Biology, Engineering, Innovation",
            "degree": "Biomedical Engineering"
        },
        {
            "name": "📊 Data Scientist",
            "description": "Uses data to solve business and scientific problems.",
            "salary": "$90k–170k/year",
            "skills": "Math, Python, Statistics",
            "degree": "Data Science or Computer Science"
        }
    ]

    for career in careers:
        with st.container(border=True):
            st.subheader(career["name"])
            st.write(career["description"])
            st.write(f"**💰 Salary:** {career['salary']}")
            st.write(f"**🧠 Skills:** {career['skills']}")
            st.write(f"**🎓 Degree:** {career['degree']}")

# -----------------------------
# ABOUT
# -----------------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About FutureMirror AI")
