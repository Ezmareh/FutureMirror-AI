import streamlit as st
import google.generativeai as genai
import json
# -----------------------------
# GEMINI SETUP
# -----------------------------

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_future(name, age, grade, subjects, interests, strengths, goals):

    prompt = f"""
You are FutureMirror AI.

A student has answered a career questionnaire.

Name: {name}
Age: {age}
Grade: {grade}

Favourite Subjects:
{", ".join(subjects)}

Interests:
{interests}

Strengths:
{strengths}

Goals:
{goals}

Your task is to generate THREE possible future career paths.

Format exactly like this.

## 🟢 Reflection Alpha

Career:
Compatibility:
Future Snapshot:
Powers You'll Need:
- item
- item
- item
- item

First Mission:
Journey Ahead:
Biggest Obstacle:
Why This Fits You:

Repeat for:

🟣 Reflection Beta

🔵 Reflection Gamma

Make each reflection different.

Be encouraging.

Avoid generic advice.

Keep the total response under 700 words.
"""

    response = model.generate_content(prompt)

    return response.text
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

        with st.spinner("🪞 Looking into your future..."):

            try:

                ai_response = generate_future(
                    name,
                    age,
                    grade,
                    subjects,
                    interests,
                    strengths,
                    goals
                )

                st.balloons()

                st.divider()

                st.markdown(ai_response)

                st.divider()

                st.caption(
                    "🪞 FutureMirror AI explores possibilities—not certainties. Your future depends on the choices you make today."
                )

            except Exception as e:

                st.error("Something went wrong while contacting the AI.")

                st.exception(e)
# -----------------------------
# CAREER LIBRARY
# -----------------------------
elif page == "📚 Career Library":

    st.title("📚 Career Library")

# -----------------------------
# ABOUT
# -----------------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About FutureMirror AI")
