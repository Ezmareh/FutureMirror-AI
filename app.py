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
# HELPER: render one reflection
# -----------------------------
def render_reflection(career, score, info):
    st.subheader(career)
    st.metric("Compatibility", f"{score}%")

    st.markdown("### 💬 Future Snapshot")
    st.info(
        f"Imagine yourself a few years from now working as a **{career}**, "
        "using your skills to make a real impact every day."
    )

    st.markdown("### 🧠 Powers You'll Need")
    for power in info["powers"]:
        st.write(f"- {power}")

    st.markdown("### 🚀 First Mission")
    st.success(info["mission"])

    # Pakistan institutes
    institutes = info.get("institutes", [])
    if institutes:
        st.markdown("#### 🏫 Where to Study in Pakistan")
        for inst in institutes:
            st.markdown(f"- [{inst['name']}]({inst['url']})")

    st.markdown("### 🎓 Journey Ahead")
    st.write(info["journey"])

    st.markdown("### ⚠ Biggest Obstacle")
    st.warning(info["obstacle"])


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
    .hero h1{ font-size:55px; margin-bottom:10px; }
    .hero h3{ font-weight:400; color:#E5E7EB; }
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

    ✅ Pakistani universities & institutes to apply to

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
    st.markdown("Answer a few questions and let FutureMirror AI explore three possible futures for you.")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        age = st.slider("Age", 13, 25, 16)
        grade = st.selectbox(
            "Current Grade",
            ["Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","University"]
        )
        subjects = st.multiselect(
            "Favorite Subjects",
            ["Mathematics","Physics","Computer Science","Biology",
             "Chemistry","Business","Economics","English","Art"]
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

    if st.button("🪞 Reveal My Futures", use_container_width=True):

        progress = st.progress(0)
        status = st.empty()

        status.write("🪞 Initializing Mirror...")
        progress.progress(20)
        time.sleep(0.8)

        status.write("🧠 Analyzing strengths...")
        progress.progress(45)
        time.sleep(0.8)

        status.write("📚 Matching careers with AI...")
        progress.progress(70)

        try:
            top_careers, career_info = recommend_careers(subjects, interests, strengths)

            progress.progress(100)
            time.sleep(0.4)
            status.success("✨ Mirror Unlocked!")

            # ── Space / rocket launch animation ──────────────────────────
            st.markdown("""
<style>
@keyframes rocketLaunch {
    0%   { bottom: 20px; opacity: 1; }
    80%  { opacity: 1; }
    100% { bottom: 200px; opacity: 0; }
}
@keyframes starTwinkle {
    0%,100% { opacity:0.15; transform:scale(0.7); }
    50%      { opacity:1;    transform:scale(1.3); }
}
@keyframes fadeIn {
    from { opacity:0; } to { opacity:1; }
}
@keyframes floatPlanet {
    0%,100% { transform:translateY(0px); }
    50%      { transform:translateY(-8px); }
}
.space-wrap {
    position:relative;
    background:linear-gradient(180deg,#03030f 0%,#0d0d2b 50%,#1a0a3d 100%);
    border-radius:20px;
    height:200px;
    overflow:hidden;
    margin:20px 0 10px 0;
    animation:fadeIn 0.4s ease;
    border:1px solid #2a1a6e;
}
.s-rocket {
    position:absolute;
    left:50%;
    transform:translateX(-50%) rotate(-45deg);
    font-size:56px;
    animation:rocketLaunch 2s ease-in forwards;
    animation-delay:0.2s;
    filter:drop-shadow(0 0 14px #ff7043);
}
.s-star {
    position:absolute;
    color:#fff;
    animation:starTwinkle linear infinite;
}
.s-planet {
    position:absolute;
    animation:floatPlanet 3s ease-in-out infinite;
}
.s-label {
    position:absolute;
    bottom:14px;
    width:100%;
    text-align:center;
    color:#c4b5fd;
    font-size:14px;
    font-weight:700;
    letter-spacing:3px;
    text-transform:uppercase;
}
</style>

<div class="space-wrap">
  <!-- Stars -->
  <span class="s-star" style="font-size:10px;top:8%;left:5%;animation-duration:1.2s;animation-delay:0.0s;">★</span>
  <span class="s-star" style="font-size:8px;top:12%;left:15%;animation-duration:1.8s;animation-delay:0.3s;">✦</span>
  <span class="s-star" style="font-size:12px;top:6%;left:28%;animation-duration:1.5s;animation-delay:0.1s;">★</span>
  <span class="s-star" style="font-size:7px;top:18%;left:42%;animation-duration:2.0s;animation-delay:0.6s;">✦</span>
  <span class="s-star" style="font-size:11px;top:9%;left:60%;animation-duration:1.3s;animation-delay:0.4s;">★</span>
  <span class="s-star" style="font-size:9px;top:20%;left:73%;animation-duration:1.7s;animation-delay:0.2s;">✦</span>
  <span class="s-star" style="font-size:8px;top:5%;left:86%;animation-duration:1.1s;animation-delay:0.8s;">★</span>
  <span class="s-star" style="font-size:13px;top:35%;left:10%;animation-duration:2.2s;animation-delay:0.5s;">✦</span>
  <span class="s-star" style="font-size:7px;top:40%;left:32%;animation-duration:1.4s;animation-delay:0.7s;">★</span>
  <span class="s-star" style="font-size:10px;top:38%;left:78%;animation-duration:1.9s;animation-delay:0.1s;">✦</span>
  <span class="s-star" style="font-size:8px;top:52%;left:55%;animation-duration:1.6s;animation-delay:0.9s;">★</span>
  <span class="s-star" style="font-size:6px;top:55%;left:90%;animation-duration:1.3s;animation-delay:0.3s;">✦</span>
  <!-- Planets -->
  <span class="s-planet" style="top:10%;left:80%;font-size:30px;animation-delay:0s;">🪐</span>
  <span class="s-planet" style="top:15%;left:3%;font-size:22px;animation-delay:1s;">🌙</span>
  <!-- Rocket -->
  <div class="s-rocket" style="bottom:20px;">🚀</div>
  <!-- Label -->
  <div class="s-label">🌌 your future is launching...</div>
</div>
""", unsafe_allow_html=True)

            st.divider()

            # ── Reflections ───────────────────────────────────────────────
            labels = [
                ("🟢 Reflection Alpha", True),
                ("🟣 Reflection Beta",  False),
                ("🔵 Reflection Gamma", False),
            ]

            for i, (label, expanded) in enumerate(labels):
                with st.expander(label, expanded=expanded):
                    career, score = top_careers[i]
                    info = career_info[career]
                    render_reflection(career, score, info)

        except Exception as e:
            progress.empty()
            status.error(f"❌ Something went wrong while generating your futures: {e}")


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
        {"name":"👨‍🏫 Teacher","description":"Educates and inspires students.","salary":"$40k–90k/year","skills":"Communication, Patience","degree":"Education"},
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


# -----------------------------
# ABOUT
# -----------------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About FutureMirror AI")

    st.markdown("""
    ## 🌟 Our Mission

    Choosing a career can feel overwhelming. FutureMirror AI was created to help students
    explore careers that match their interests, strengths, and favourite subjects.

    Instead of telling users what they *must* become, FutureMirror AI encourages them to
    discover multiple possibilities and start thinking about their future.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Features")
        st.write("✅ Personalized career recommendations")
        st.write("✅ Three future career reflections")
        st.write("✅ Career Library with 30 professions")
        st.write("✅ Pakistani institute suggestions per career")
        st.write("✅ Simple and interactive interface")

    with col2:
        st.subheader("🛠 Technologies Used")
        st.write("• Python")
        st.write("• Streamlit")
        st.write("• Groq API (LLaMA 3.3 70B)")

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.info("""
**Project:** FutureMirror AI

**Version:** 1.0

**Developed By:** Ezmareh Rehman

FutureMirror AI was built as a school project to demonstrate how technology can help students make more informed career decisions.
""")

    st.divider()

    st.success("✨ Thank you for exploring FutureMirror AI. Your future starts with the choices you make today.")
