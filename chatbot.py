import streamlit as st
import re

st.set_page_config(
    page_title="Workshop Registration Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- PROFESSIONAL CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f8fc;
    color: #172b4d;
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5ebf3;
}

.hero {
    background: linear-gradient(120deg, #ffffff, #edf6ff);
    padding: 35px;
    border-radius: 22px;
    border: 1px solid #dceaff;
    margin-bottom: 25px;
}

.hero h1 {
    color: #163b70;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    color: #64748b;
    font-size: 16px;
    line-height: 1.7;
}

.section-title {
    font-size: 24px;
    font-weight: 750;
    color: #163b70;
    margin: 15px 0;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e3eaf4;
    min-height: 155px;
    margin-bottom: 12px;
}

.info-card h3 {
    color: #1d4ed8;
    font-size: 19px;
}

.info-card p {
    color: #64748b;
    font-size: 14px;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 30px;
    background: #dbeafe;
    color: #1d4ed8;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 12px;
}

div.stButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    min-height: 42px;
}

div.stButton > button:hover {
    background: #1d4ed8;
    color: white;
}

div[data-testid="stFormSubmitButton"] button {
    background: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 700;
    width: 100%;
}

.footer {
    text-align: center;
    color: #94a3b8;
    padding: 25px 0;
    font-size: 12px;
}

div[data-testid="stChatMessage"] {
    background: white;
    border: 1px solid #e5ebf3;
    border-radius: 14px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- WORKSHOP DATA ----------
workshops = {
    "Python Programming": {
        "description": "Learn Python fundamentals, variables, loops, functions and practical coding.",
        "duration": "2 days",
        "level": "Beginner",
        "icon": "🐍"
    },
    "Artificial Intelligence": {
        "description": "Explore AI fundamentals, real-world applications and intelligent systems.",
        "duration": "3 days",
        "level": "Beginner",
        "icon": "🤖"
    },
    "Web Development": {
        "description": "Discover HTML, CSS and JavaScript while learning how websites are built.",
        "duration": "2 days",
        "level": "Beginner",
        "icon": "💻"
    },
    "Cyber Security": {
        "description": "Understand online safety, cybersecurity fundamentals and common threats.",
        "duration": "2 days",
        "level": "Beginner",
        "icon": "🔐"
    }
}

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "registered" not in st.session_state:
    st.session_state.registered = False

if "registration_info" not in st.session_state:
    st.session_state.registration_info = None

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🎓 WorkshopHub")
    st.caption("Workshop Registration Assistant")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🤖 AI Assistant",
            "📝 Register",
            "📚 Explore Workshops"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### 💡 Need help?")
    st.write("Ask the assistant about workshops, duration, certificates or registration.")

    st.divider()
    st.caption("Academic Project · Demo Version")

# ---------- HOME ----------
if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <span class="badge">WORKSHOP REGISTRATION PORTAL</span>
        <h1>Learn Something New.<br>Build Your Future.</h1>
        <p>
        Discover practical workshops, explore new technologies and take
        the next step in your learning journey. Use our assistant to get
        quick answers or explore the available workshops.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Your learning starts here</div>',
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📚 Explore</h3>
            <p>Discover workshops in programming, AI, web development and cybersecurity.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🤖 Get Answers</h3>
            <p>Ask our workshop assistant about topics, duration and registration.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>📝 Register</h3>
            <p>Complete the demo registration form and see your submission confirmation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Featured Workshops</div>',
                unsafe_allow_html=True)

    cols = st.columns(2)

    for i, (name, details) in enumerate(workshops.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="info-card">
                <h3>{details['icon']} {name}</h3>
                <p>{details['description']}</p>
                <span class="badge">{details['duration']} · {details['level']}</span>
            </div>
            """, unsafe_allow_html=True)

    if st.button("Explore All Workshops →"):
        st.info("Choose 'Explore Workshops' from the sidebar.")

# ---------- WORKSHOP EXPLORER ----------
elif page == "📚 Explore Workshops":

    st.markdown("""
    <div class="hero">
        <h1>Explore Workshops</h1>
        <p>Find a topic that interests you and start learning something new.</p>
    </div>
    """, unsafe_allow_html=True)

    for name, details in workshops.items():
        with st.container(border=True):
            left, right = st.columns([4, 1])

            with left:
                st.subheader(f"{details['icon']} {name}")
                st.write(details["description"])
                st.caption(
                    f"Duration: {details['duration']}  ·  "
                    f"Level: {details['level']}"
                )

            with right:
                st.write("")
                st.write("")
                if st.button("Register", key=f"reg_{name}"):
                    st.session_state.selected_workshop = name
                    st.info(
                        "Select **📝 Register** from the sidebar to "
                        "complete the form for this workshop."
                    )

# ---------- REGISTRATION ----------
elif page == "📝 Register":

    st.markdown("""
    <div class="hero">
        <h1>Workshop Registration</h1>
        <p>Fill in the form below to try the registration process.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.registered:
        st.success("Registration demo completed successfully! 🎉")

        st.markdown("### Submission Summary")
        st.write(f"**Name:** {st.session_state.registration_info['name']}")
        st.write(f"**Email:** {st.session_state.registration_info['email']}")
        st.write(f"**College:** {st.session_state.registration_info['college']}")
        st.write(f"**Workshop:** {st.session_state.registration_info['workshop']}")

        st.info(
            "This is a demonstration project. Registration details are not "
            "saved to a database and will not be available as permanent records."
        )

        if st.button("Start a New Demo Registration"):
            st.session_state.registered = False
            st.session_state.registration_info = None
            st.rerun()

    else:
        st.markdown("### 👤 Participant Information")

        with st.form("registration_form"):
            name = st.text_input("Full Name", placeholder="Enter your full name")
            email = st.text_input("Email Address", placeholder="you@example.com")
            college = st.text_input("College / Institution", placeholder="Enter your college")

            selected_default = st.session_state.get(
                "selected_workshop", "Python Programming"
            )

            workshop_names = list(workshops.keys())
            default_index = (
                workshop_names.index(selected_default)
                if selected_default in workshop_names else 0
            )

            workshop = st.selectbox(
                "Choose a Workshop",
                workshop_names,
                index=default_index
            )

            agree = st.checkbox(
                "I understand this is a demonstration registration form."
            )

            submitted = st.form_submit_button("Submit Registration")

            if submitted:
                if not name.strip() or not email.strip() or not college.strip():
                    st.error("Please complete all fields before submitting.")

                elif not re.match(r"^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$", email.strip()):
                    st.error("Please enter a valid email address.")

                elif not agree:
                    st.warning("Please confirm that you understand this is a demo.")

                else:
                    st.session_state.registration_info = {
                        "name": name.strip(),
                        "email": email.strip(),
                        "college": college.strip(),
                        "workshop": workshop
                    }
                    st.session_state.registered = True
                    st.rerun()

        st.caption(
            "Privacy note: This demo does not use a database or permanently "
            "store registration submissions."
        )

# ---------- CHATBOT ----------
elif page == "🤖 AI Assistant":

    st.markdown("""
    <div class="hero">
        <h1>Workshop Assistant</h1>
        <p>Ask questions about available workshops, registration, duration and certificates.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Try asking")

    suggestions = [
        "What workshops are available?",
        "Tell me about Python",
        "How do I register?",
        "Are certificates available?"
    ]

    suggestion_cols = st.columns(2)

    for i, suggestion in enumerate(suggestions):
        with suggestion_cols[i % 2]:
            if st.button(suggestion, key=f"suggestion_{i}"):
                st.session_state.pending_question = suggestion

    def get_response(question):
        q = question.lower()

        if any(word in q for word in ["hello", "hi", "hey", "namaste"]):
            return (
                "Hello! 👋 Welcome to WorkshopHub. I can help you explore "
                "workshops, understand their duration and learn how to register."
            )

        if "available" in q or "list" in q or "workshops" in q:
            return (
                "We currently feature these workshops:\n\n"
                + "\n".join(
                    f"- {details['icon']} **{name}** — {details['duration']}"
                    for name, details in workshops.items()
                )
                + "\n\nVisit **Explore Workshops** for more details."
            )

        if "python" in q:
            return (
                "🐍 **Python Programming**\n\n"
                "Learn variables, loops, functions and basic programming concepts. "
                "Duration: **2 days**. Level: **Beginner**."
            )

        if "artificial intelligence" in q or re.search(r"\\bai\\b", q):
            return (
                "🤖 **Artificial Intelligence**\n\n"
                "Explore AI fundamentals, intelligent systems and real-world "
                "applications. Duration: **3 days**. Level: **Beginner**."
            )

        if "web" in q or "website" in q:
            return (
                "💻 **Web Development**\n\n"
                "Discover HTML, CSS and JavaScript and learn how websites "
                "are created. Duration: **2 days**."
            )

        if "cyber" in q or "security" in q:
            return (
                "🔐 **Cyber Security**\n\n"
                "Learn about online safety, cybersecurity fundamentals and "
                "common digital threats. Duration: **2 days**."
            )

        if "register" in q or "registration" in q or "sign up" in q:
            return (
                "📝 To try registering, open **Register** in the sidebar. "
                "Fill in your name, email, college and selected workshop, "
                "then submit the form. This demo does not permanently save details."
            )

        if "certificate" in q:
            return (
                "Certificate availability has not been configured for this demo. "
                "Please confirm certificate details with the workshop organiser."
            )

        if "duration" in q or "long" in q or "days" in q:
            return (
                "Workshop durations in this demo:\n\n"
                "- Python Programming: 2 days\n"
                "- Artificial Intelligence: 3 days\n"
                "- Web Development: 2 days\n"
                "- Cyber Security: 2 days"
            )

        if "fee" in q or "price" in q or "cost" in q:
            return (
                "Workshop fees have not been configured in this demo. "
                "Please contact the workshop organiser for confirmed pricing."
            )

        if "thank" in q:
            return "You're welcome! 😊 Feel free to ask anything about our workshops."

        return (
            "I can help with workshop details, duration, registration and "
            "general FAQs. Try asking: 'Tell me about Python' or "
            "'How do I register?'\n\n"
            "Note: I'm a rule-based demo assistant, so I answer using predefined information."
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    pending = st.session_state.pop("pending_question", None)
    user_input = st.chat_input("Ask about workshops...")

    question = pending or user_input

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = get_response(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    WorkshopHub · Workshop Registration Assistant<br>
    Academic Demonstration Project
</div>
""", unsafe_allow_html=True)
