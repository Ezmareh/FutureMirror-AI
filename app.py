import streamlit as st
import time
from openai import OpenAI

# -----------------------------
# GEMINI / OPENROUTER SETUP
# -----------------------------

client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

# -----------------------------
# AI FUNCTION (FIXED)
# -----------------------------

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

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    return response.choices[0].message.content


# -----------------------------
# PAGE CONFIG
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
    ["🏠 Home", "🪞 Discover My Future", "📚 Career Library", "ℹ️ About"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")

# -----------------------------
# HOME PAGE
# -----------------------------

if page == "🏠 Home":

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#4F46E5,#7C3AED);
        padding:45px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">
    <h1>🪞 FutureMirror AI</h1>
    <h3>Who could you become tomorrow?</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🌍 Why FutureMirror AI?

    Choosing a career is one of the biggest decisions a student will ever make.

    **FutureMirror AI helps students explore personalized career paths.**
    """)

    st.success("👉 Go to Discover My Future from sidebar")

# -----------------------------
# DISCOVER PAGE
# -----------------------------

elif page == "🪞 Discover My Future":

    st.title("🪞 Discover My Future")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        age = st.slider("Age", 13, 25, 16)

        grade = st.selectbox(
            "Current Grade",
            ["Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12", "University"]
        )

        subjects = st.multiselect(
            "Favorite Subjects",
            ["Mathematics", "Physics", "Computer Science", "Biology", "Chemistry", "Business"]
        )

    with col2:
        interests = st.text_area("Interests")
        strengths = st.text_area("Strengths")
        goals = st.text_area("Goals")

    if st.button("🪞 Reveal My Futures"):

        progress = st.progress(0)
        status = st.empty()

        status.write("Analyzing...")
        progress.progress(30)
        time.sleep(1)

        status.write("Matching careers...")
        progress.progress(70)
        time.sleep(1)

        status.write("Generating futures...")
        progress.progress(100)
        time.sleep(1)

        try:
            with st.spinner("Thinking..."):
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
            st.markdown(ai_response)

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
