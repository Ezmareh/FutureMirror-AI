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

    st.title("🪞 FutureMirror AI")

    st.subheader("Who could you become tomorrow?")

    st.markdown(
        """
        ### A normal mirror reflects who you are today.

        ## FutureMirror AI reflects who you could become tomorrow.

        Explore personalized career paths based on your interests,
        strengths, and ambitions.
        """
    )

    st.info(
        "The future isn't fixed. These are possibilities, not predictions."
    )

    st.divider()

    st.success("Click **Discover My Future** in the sidebar to begin!")

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
