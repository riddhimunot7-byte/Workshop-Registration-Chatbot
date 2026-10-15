import streamlit as st

st.set_page_config(
    page_title="Workshop AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM UI ----------
st.markdown("""
<style>
.stApp {
    background: #f4f7fc;
    color: #172554;
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e2e8f0;
}

h1, h2, h3 {
    color: #173b75 !important;
}

p, label {
    color: #334155;
}

.hero {
    background: linear-gradient(120deg, #173b75, #3678d4);
    padding: 32px;
    border-radius: 20px;
    color: white;
    margin-bottom: 24px;
}

.hero h1, .hero p {
    color: white !important;
}

.card {
    background: white;
    padding: 22px;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    margin-bottom: 14px;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #1d4ed8;
    color: white;
}

[data-testid="stChatMessage"] {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 12px;
}

input, textarea {
    border-radius: 10px !important;
}

.footer {
    color: #64748b;
    text-align: center;
    padding: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🎓 Workshop AI")
    st.caption("Your learning companion")
    st.divider()

    page = st.radio(
        "MENU",
        ["AI Assistant", "Register", "Explore Workshops"]
    )

    st.divider()
    st.info("💡 Ask questions about workshops, registration, and learning.")

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>Workshop Registration Assistant</h1>
    <p>Discover workshops, explore new skills, and get started in minutes.</p>
</div>
""", unsafe_allow_html=True)

# ---------- AI ASSISTANT ----------
if page == "AI Assistant":
    st.subheader("💬 How can I help you?")
    st.write("Ask me about available workshops or registration.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Type your question here...")

    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        q = prompt.lower()

        if "python" in q:
            answer = (
                "**Python Programming** 🐍\n\n"
                "Explore programming fundamentals, variables, loops, "
                "functions, and beginner-friendly projects."
            )
        elif "ai" in q or "machine learning" in q:
            answer = (
                "**Artificial Intelligence** 🤖\n\n"
                "Learn about AI concepts, machine learning fundamentals, "
                "and real-world applications."
            )
        elif "web" in q:
            answer = (
                "**Web Development** 🌐\n\n"
                "Discover HTML, CSS, JavaScript, and the basics of "
                "building interactive websites."
            )
        elif "cyber" in q or "security" in q:
            answer = (
                "**Cyber Security** 🔐\n\n"
                "Explore online safety, security fundamentals, "
                "and cyber awareness."
            )
        elif "register" in q or "registration" in q:
            answer = (
                "📝 Select **Register** from the sidebar to open "
                "the workshop registration form."
            )
        elif any(word in q for word in ["hello", "hi", "hey"]):
            answer = (
                "Hello! 👋 Welcome to Workshop AI. "
                "Would you like to explore Python, AI, Web Development, "
                "Cyber Security, or registration?"
            )
        elif "duration" in q or "timing" in q:
            answer = (
                "Workshop timings and duration depend on the organiser. "
                "Please check the official event schedule for confirmation."
            )
        elif "certificate" in q:
            answer = (
                "Certificate availability depends on the workshop organiser. "
                "Please confirm this with the event team."
            )
        else:
            answer = (
                "I can help you explore Python Programming, Artificial "
                "Intelligence, Web Development, Cyber Security, and "
                "registration. Which topic interests you?"
            )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

# ---------- REGISTRATION ----------
elif page == "Register":
    st.subheader("📝 Workshop Registration")
    st.write("Complete the form to see your registration confirmation.")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        college = st.text_input("College / Institution")

        workshop = st.selectbox(
            "Select Workshop",
            [
                "Python Programming",
                "Artificial Intelligence",
                "Web Development",
                "Cyber Security"
            ]
        )

        submitted = st.form_submit_button("Submit Registration")

    if submitted:
        if not name.strip() or not college.strip():
            st.error("Please enter your name and college.")
        elif "@" not in email or "." not in email.split("@")[-1]:
            st.error("Please enter a valid email address.")
        else:
            st.success("🎉 Registration submitted successfully!")
            st.markdown(
                f"""
                <div class="card">
                    <h3>Registration Confirmation</h3>
                    <p><b>Name:</b> {name}</p>
                    <p><b>Workshop:</b> {workshop}</p>
                    <p>Thank you for your interest!</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.caption(
                "Demo mode: registration details are not permanently stored."
            )

# ---------- WORKSHOPS ----------
elif page == "Explore Workshops":
    st.subheader("✨ Explore Our Workshops")
    st.write("Choose a topic and discover the skills you can explore.")

    workshops = [
        (
            "🐍 Python Programming",
            "Learn programming basics, loops, functions, and problem-solving."
        ),
        (
            "🤖 Artificial Intelligence",
            "Discover AI, machine learning, and intelligent applications."
        ),
        (
            "🌐 Web Development",
            "Explore HTML, CSS, JavaScript, and website fundamentals."
        ),
        (
            "🔐 Cyber Security",
            "Understand cyber awareness, digital safety, and security basics."
        )
    ]

    for title, description in workshops:
        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="footer">🎓 Workshop AI Assistant · Interactive Demo</div>',
    unsafe_allow_html=True
)
