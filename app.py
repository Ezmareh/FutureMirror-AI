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
    st.markdown("Explore a variety of exciting careers and discover what each one involves.")

    careers = [

        {"name":"👨‍⚕️ Doctor","description":"Diagnoses illnesses and treats patients.","salary":"$80k–250k/year","skills":"Biology, Empathy, Communication","degree":"Medicine (MBBS/MD)"},
        {"name":"🩺 Nurse","description":"Provides patient care and supports doctors.","salary":"$50k–100k/year","skills":"Compassion, Teamwork","degree":"Nursing"},
        {"name":"🦷 Dentist","description":"Treats teeth and oral health problems.","salary":"$90k–220k/year","skills":"Precision, Biology","degree":"Dentistry"},
        {"name":"🧠 Psychologist","description":"Helps improve mental health and wellbeing.","salary":"$60k–130k/year","skills":"Listening, Empathy","degree":"Psychology"},
        {"name":"💊 Pharmacist","description":"Dispenses medicines and advises patients.","salary":"$80k–140k/year","skills":"Chemistry, Attention to Detail","degree":"Pharmacy"},
        {"name":"🧬 Biomedical Engineer","description":"Designs medical devices and healthcare technology.","salary":"$80k–150k/year","skills":"Biology, Engineering","degree":"Biomedical Engineering"},
        {"name":"🤖 AI Engineer","description":"Develops artificial intelligence systems.","salary":"$100k–200k/year","skills":"Python, Machine Learning","degree":"Computer Science"},
        {"name":"💻 Software Engineer","description":"Builds software and applications.","salary":"$90k–180k/year","skills":"Programming, Problem Solving","degree":"Computer Science"},
        {"name":"🌐 Web Developer","description":"Creates websites and web applications.","salary":"$60k–130k/year","skills":"HTML, CSS, JavaScript","degree":"Computer Science"},
        {"name":"📱 Mobile App Developer","description":"Builds Android and iOS applications.","salary":"$80k–160k/year","skills":"Flutter, Java, Swift","degree":"Computer Science"},
        {"name":"📊 Data Scientist","description":"Uses data to solve real-world problems.","salary":"$90k–170k/year","skills":"Python, Statistics","degree":"Data Science"},
        {"name":"🔒 Cybersecurity Analyst","description":"Protects organizations from cyber attacks.","salary":"$90k–170k/year","skills":"Networking, Security","degree":"Cybersecurity"},
        {"name":"☁️ Cloud Engineer","description":"Builds and manages cloud infrastructure.","salary":"$100k–180k/year","skills":"AWS, Azure","degree":"Computer Science"},
        {"name":"⚙️ Mechanical Engineer","description":"Designs machines and mechanical systems.","salary":"$70k–150k/year","skills":"Physics, CAD","degree":"Mechanical Engineering"},
        {"name":"🏗️ Civil Engineer","description":"Designs roads, bridges and buildings.","salary":"$70k–140k/year","skills":"Math, Engineering","degree":"Civil Engineering"},
        {"name":"⚡ Electrical Engineer","description":"Designs electrical systems and electronics.","salary":"$80k–150k/year","skills":"Circuits, Physics","degree":"Electrical Engineering"},
        {"name":"🧪 Chemical Engineer","description":"Develops industrial chemical processes.","salary":"$80k–150k/year","skills":"Chemistry, Math","degree":"Chemical Engineering"},
        {"name":"✈️ Aerospace Engineer","description":"Designs aircraft and spacecraft.","salary":"$100k–180k/year","skills":"Physics, Engineering","degree":"Aerospace Engineering"},
        {"name":"💼 Entrepreneur","description":"Starts and grows successful businesses.","salary":"Varies","skills":"Leadership, Creativity","degree":"Business (optional)"},
        {"name":"📈 Business Analyst","description":"Improves businesses using data and strategy.","salary":"$70k–140k/year","skills":"Analysis, Communication","degree":"Business"},
        {"name":"💰 Accountant","description":"Manages financial records and taxes.","salary":"$60k–120k/year","skills":"Math, Accuracy","degree":"Accounting"},
        {"name":"📣 Marketing Manager","description":"Promotes products, services and brands.","salary":"$70k–150k/year","skills":"Communication, Creativity","degree":"Marketing"},
        {"name":"⚖️ Lawyer","description":"Represents clients and provides legal advice.","salary":"$80k–200k/year","skills":"Critical Thinking, Speaking","degree":"Law"},
        {"name":"🏛️ Architect","description":"Designs buildings and modern structures.","salary":"$70k–150k/year","skills":"Design, Creativity","degree":"Architecture"},
        {"name":"🎨 Graphic Designer","description":"Creates logos, posters and digital artwork.","salary":"$50k–100k/year","skills":"Adobe Suite, Creativity","degree":"Graphic Design"},
        {"name":"🖥️ UX Designer","description":"Designs user-friendly digital experiences.","salary":"$80k–150k/year","skills":"UI/UX, Research","degree":"Design or Computer Science"},
        {"name":"🎬 Animator","description":"Creates animations for films and games.","salary":"$60k–120k/year","skills":"Animation, Creativity","degree":"Animation"},
        {"name":"🎮 Game Developer","description":"Builds exciting video games.","salary":"$70k–150k/year","skills":"Programming, Game Design","degree":"Computer Science"},
        {"name":"📰 Journalist","description":"Researches and reports news stories.","salary":"$45k–100k/year","skills":"Writing, Investigation","degree":"Journalism"},
        {"name":"👨‍🏫 Teacher","description":"Educates and inspires students.","salary":"$40k–90k/year","skills":"Communication, Patience","degree":"Education"}

    ]

    search = st.text_input("🔍 Search a career")

    for career in careers:

        if search.lower() in career["name"].lower():

            with st.container(border=True):

                st.subheader(career["name"])

                st.write(career["description"])

                st.write(f"**💰 Average Salary:** {career['salary']}")

                st.write(f"**🧠 Skills Needed:** {career['skills']}")

                st.write(f"**🎓 Degree:** {career['degree']}")
```

# -----------------------------
# ABOUT
# -----------------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About FutureMirror AI")
