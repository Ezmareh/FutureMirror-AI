import streamlit as st

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

    st.title("🪞 Discover My Future")

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
