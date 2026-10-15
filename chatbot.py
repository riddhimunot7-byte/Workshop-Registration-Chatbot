import streamlit as st

st.set_page_config(
    page_title="Workshop AI Assistant",
    page_icon="💜",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100b24, #21113d, #101827);
    color: #ffffff;
}
[data-testid="stSidebar"] {
    background: #17102b;
}
h1, h2, h3, p, label {
    color: #f5f0ff !important;
}
div.stButton > button {
    background: linear-gradient(90deg, #8b5cf6, #c084fc);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
}
div.stButton > button:hover {
    border: 1px solid #e9d5ff;
    color: white;
}
div[data-testid="stForm"] {
    background: #21183a;
    border: 1px solid #6544a5;
    padding: 20px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("💜 Workshop AI")
    st.write("Your workshop companion")
    st.divider()
    page = st.radio(
        "Navigate",
        ["AI Assistant", "Register", "Workshop Info"]
    )
    st.caption("✨ Learn. Connect. Build.")

st.title("💜 Workshop Registration Assistant")
st.write("Your smart companion for discovering workshops and getting started.")

if page == "AI Assistant":
    st.subheader("🤖 Chat with the Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask me about workshops...")

    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        q = prompt.lower()

        if "python" in q:
            answer = "🐍 **Python Workshop**\n\nLearn Python basics, variables, loops, functions, and build beginner-friendly projects."
        elif "ai" in q or "machine learning" in q:
            answer = "🤖 **AI & Machine Learning Workshop**\n\nExplore AI concepts, machine learning basics, and real-world applications."
        elif "web" in q:
            answer = "🌐 **Web Development Workshop**\n\nLearn HTML, CSS, and JavaScript to create interactive websites."
        elif "cyber" in q or "security" in q:
            answer = "🔐 **Cyber Security Workshop**\n\nDiscover online safety, security fundamentals, and common cyber threats."
        elif "register" in q or "registration" in q:
            answer = "📝 Open the **Register** section from the sidebar to fill out the workshop registration form."
        elif any(word in q for word in ["hello", "hi", "hey"]):
            answer = "Hey there! 👋 Welcome! Ask me about Python, AI, Web Development, Cyber Security, or registration."
        elif "duration" in q or "time" in q:
            answer = "⏰ Workshop duration depends on the event schedule. Please check with the workshop organiser for confirmed timings."
        elif "college" in q or "certificate" in q:
            answer = "🎓 For college-specific details and certificates, please contact the workshop organiser."
        else:
            answer = "💜 I can help with Python, AI & Machine Learning, Web Development, Cyber Security, and registration. What would you like to explore?"

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

elif page == "Register":
    st.subheader("📝 Workshop Registration")
    st.write("Complete this demo form to see your confirmation.")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        college = st.text_input("College Name")

        workshop = st.selectbox(
            "Choose Your Workshop",
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
            st.error("Please fill in your name and college.")
        elif "@" not in email or "." not in email.split("@")[-1]:
            st.error("Please enter a valid email address.")
        else:
            st.success("🎉 Registration submitted successfully!")
            st.info(
                f"Thank you, {name}! You selected **{workshop}**."
            )
            st.caption(
                "Demo only: your details are not permanently stored."
            )

elif page == "Workshop Info":
    st.subheader("✨ Explore Our Workshops")

    workshops = [
        ("🐍 Python Programming", "Programming fundamentals, loops, functions, and beginner projects."),
        ("🤖 Artificial Intelligence", "AI concepts, machine learning basics, and practical applications."),
        ("🌐 Web Development", "HTML, CSS, JavaScript, and website development."),
        ("🔐 Cyber Security", "Digital safety, security basics, and cyber awareness.")
    ]

    for title, description in workshops:
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.write(description)

st.divider()
st.caption("💜 Workshop AI Assistant | Interactive Demo")
