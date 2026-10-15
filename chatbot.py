import streamlit as st
import re

st.set_page_config(
    page_title="WorkshopHub | Learn & Grow",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- WORKSHOP DATA --------------------

WORKSHOPS = {
    "Python Programming": {
        "icon": "🐍",
        "category": "PROGRAMMING",
        "duration": "2 Days",
        "level": "Beginner",
        "description": (
            "Master Python basics, variables, loops, functions "
            "and problem-solving."
        ),
        "color": "#E8F2FF"
    },
    "Artificial Intelligence": {
        "icon": "🤖",
        "category": "ARTIFICIAL INTELLIGENCE",
        "duration": "3 Days",
        "level": "Beginner",
        "description": (
            "Explore AI fundamentals, intelligent systems "
            "and real-world applications."
        ),
        "color": "#F0EAFE"
    },
    "Web Development": {
        "icon": "💻",
        "category": "WEB TECHNOLOGY",
        "duration": "2 Days",
        "level": "Beginner",
        "description": (
            "Discover HTML, CSS and JavaScript and learn "
            "how modern websites are built."
        ),
        "color": "#E5F8F1"
    },
    "Cyber Security": {
        "icon": "🔐",
        "category": "DIGITAL SECURITY",
        "duration": "2 Days",
        "level": "Beginner",
        "description": (
            "Understand online safety, cybersecurity "
            "fundamentals and common digital threats."
        ),
        "color": "#FFF0E7"
    }
}

# -------------------- SESSION STATE --------------------

defaults = {
    "page": "Home",
    "messages": [],
    "registration": None,
    "selected_workshop": "Python Programming",
    "pending_question": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #142D4E;
    --blue: #316BEB;
    --muted: #718096;
    --border: #E4EAF3;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F7F9FD;
    color: var(--navy);
}

[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.navbar {
    background: #FFFFFF;
    border: 1px solid #E6ECF5;
    border-radius: 16px;
    padding: 16px 22px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
}

.brand {
    font-size: 22px;
    font-weight: 800;
    color: #17365F;
    white-space: nowrap;
}

.brand span {
    color: #3975ED;
}

.brand-subtitle {
    font-size: 10px;
    color: #8795A9;
    letter-spacing: 1.4px;
    margin-top: 3px;
}

.hero {
    background: linear-gradient(115deg, #FFFFFF 15%, #EAF3FF 75%, #F1EDFF);
    border: 1px solid #DDE8F8;
    border-radius: 24px;
    padding: 42px;
    margin-bottom: 30px;
}

.eyebrow {
    display: inline-block;
    color: #285CC7;
    background: #E0EBFF;
    border-radius: 30px;
    padding: 8px 13px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}

.hero h1 {
    color: #17365F;
    font-size: clamp(34px, 5vw, 52px);
    font-weight: 800;
    line-height: 1.15;
    margin: 22px 0 14px;
    letter-spacing: -1.5px;
}

.gradient-text {
    color: #3975ED;
}

.hero p {
    color: #687991;
    line-height: 1.85;
    font-size: 15px;
    max-width: 680px;
}

.section-heading {
    color: #17365F;
    font-size: 27px;
    font-weight: 800;
    margin: 12px 0 7px;
}

.section-subtitle {
    color: #718096;
    font-size: 14px;
    margin-bottom: 22px;
}

.workshop-card {
    background: white;
    border: 1px solid #E4EAF3;
    border-radius: 19px;
    padding: 23px;
    min-height: 245px;
    margin-bottom: 12px;
    transition: 0.2s ease;
}

.workshop-card:hover {
    border-color: #9DBCF7;
    box-shadow: 0 10px 30px rgba(36, 83, 151, 0.08);
}

.workshop-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 54px;
    height: 54px;
    border-radius: 15px;
    font-size: 27px;
    margin-bottom: 15px;
}

.category {
    color: #5378BC;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.workshop-card h3 {
    color: #17365F;
    font-size: 19px;
    margin: 10px 0;
    font-weight: 750;
}

.workshop-card p {
    color: #718096;
    font-size: 13px;
    line-height: 1.7;
    min-height: 65px;
}

.meta {
    color: #62748C;
    font-size: 12px;
    font-weight: 600;
    margin-top: 12px;
}

.feature-card {
    background: #FFFFFF;
    border: 1px solid #E4EAF3;
    border-radius: 16px;
    padding: 22px;
    min-height: 145px;
    margin-bottom: 12px;
}

.feature-card h3 {
    color: #17365F;
    font-size: 16px;
    font-weight: 750;
}

.feature-card p {
    color: #718096;
    font-size: 13px;
    line-height: 1.7;
}

.info-banner {
    background: #EDF4FF;
    border: 1px solid #DCE9FF;
    padding: 19px 22px;
    border-radius: 15px;
    margin: 20px 0;
    color: #28528D;
    line-height: 1.7;
}

.footer {
    border-top: 1px solid #E4EAF3;
    padding-top: 22px;
    margin-top: 38px;
    text-align: center;
    color: #8996A8;
    font-size: 12px;
    line-height: 2;
}

div.stButton > button {
    border-radius: 10px;
    font-weight: 650;
    min-height: 42px;
    transition: 0.2s ease;
}

div.stButton > button[kind="primary"] {
    background: #316BEB;
    color: white;
    border: 1px solid #316BEB;
}

div.stButton > button[kind="primary"]:hover {
    background: #2457C6;
    border-color: #2457C6;
}

div.stButton > button[kind="secondary"] {
    background: white;
    color: #24456E;
    border: 1px solid #DCE5F1;
}

div[data-testid="stForm"] {
    background: #FFFFFF;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #E4EAF3;
}

div[data-testid="stChatMessage"] {
    background: #FFFFFF;
    border: 1px solid #E4EAF3;
    border-radius: 14px;
}

[data-testid="stChatInput"] {
    border-radius: 15px;
}

@media (max-width: 700px) {
    .hero {
        padding: 25px;
    }

    .navbar {
        padding: 13px;
    }

    .brand {
        font-size: 18px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- NAVIGATION --------------------

def navigate(page):
    st.session_state.page = page
    st.rerun()


nav_left, nav_middle, nav_right = st.columns([2.0, 4.8, 1.5])

with nav_left:
    st.markdown("""
    <div style="padding-top:5px">
        <div class="brand">🎓 Workshop<span>Hub</span></div>
        <div class="brand-subtitle">LEARN · BUILD · GROW</div>
    </div>
    """, unsafe_allow_html=True)

with nav_middle:
    n1, n2, n3, n4 = st.columns(4)

    with n1:
        if st.button("🏠 Home", use_container_width=True):
            navigate("Home")

    with n2:
        if st.button("📚 Workshops", use_container_width=True):
            navigate("Workshops")

    with n3:
        if st.button("🤖 Assistant", use_container_width=True):
            navigate("Assistant")

    with n4:
        if st.button("📝 Register", use_container_width=True):
            navigate("Register")

with nav_right:
    st.markdown(
        "<div style='text-align:right;padding-top:10px;"
        "color:#74849B;font-size:12px;font-weight:600'>"
        "● Demo Portal</div>",
        unsafe_allow_html=True
    )

st.divider()


# -------------------- HOME PAGE --------------------

def home_page():

    st.markdown("""
    <div class="hero">
        <span class="eyebrow">✨ YOUR LEARNING JOURNEY STARTS HERE</span>
        <h1>Discover Skills.<br>
        <span class="gradient-text">Build Your Future.</span></h1>
        <p>
        Explore technology workshops, discover new interests and develop
        practical skills. Your next learning opportunity is just a click away.
        </p>
    </div>
    """, unsafe_allow_html=True)

    hero_left, hero_right = st.columns([1.2, 1])

    with hero_left:
        if st.button(
            "📚  Explore Workshops  →",
            type="primary",
            use_container_width=True
        ):
            navigate("Workshops")

    with hero_right:
        if st.button(
            "🤖  Chat with Assistant",
            use_container_width=True
        ):
            navigate("Assistant")

    st.write("")

    st.markdown(
        '<div class="section-heading">Explore Our Workshops</div>'
        '<div class="section-subtitle">'
        'Practical learning opportunities for curious minds.</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for i, (name, data) in enumerate(WORKSHOPS.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="workshop-card">
                <div class="workshop-icon"
                     style="background:{data['color']}">
                    {data['icon']}
                </div>
                <div class="category">{data['category']}</div>
                <h3>{name}</h3>
                <p>{data['description']}</p>
                <div class="meta">
                    🕒 {data['duration']} &nbsp; · &nbsp;
                    🎯 {data['level']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"Explore {name} →",
                key=f"home_{name}",
                use_container_width=True
            ):
                st.session_state.selected_workshop = name
                navigate("Workshops")

    st.markdown(
        '<div class="section-heading">Why WorkshopHub?</div>'
        '<div class="section-subtitle">'
        'Everything you need to explore your next learning opportunity.'
        '</div>',
        unsafe_allow_html=True
    )

    f1, f2, f3 = st.columns(3)

    features = [
        ("🎯", "Easy Discovery",
         "Explore workshops by topic, duration and skill level."),
        ("💬", "Interactive Assistant",
         "Get quick answers to common workshop questions."),
        ("📝", "Simple Registration",
         "Try the guided registration process in a few steps.")
    ]

    for col, (icon, title, desc) in zip([f1, f2, f3], features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{icon} &nbsp; {title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-banner">
        <strong>💡 Start exploring today!</strong><br>
        Choose a workshop that interests you or ask our assistant
        for more information.
    </div>
    """, unsafe_allow_html=True)


# -------------------- WORKSHOPS PAGE --------------------

def workshops_page():

    st.markdown("""
    <div class="hero">
        <span class="eyebrow">📚 FIND YOUR NEXT SKILL</span>
        <h1>Explore <span class="gradient-text">Workshops.</span></h1>
        <p>
        Browse our featured technology workshops, discover what you can learn
        and choose a topic that matches your interests.
        </p>
    </div>
    """, unsafe_allow_html=True)

    for name, data in WORKSHOPS.items():

        with st.container(border=True):
            left, right = st.columns([4, 1])

            with left:
                st.markdown(
                    f"### {data['icon']} {name}"
                )
                st.write(data["description"])
                st.caption(
                    f"🕒 {data['duration']}  ·  "
                    f"🎯 {data['level']}  ·  "
                    f"📘 {data['category'].title()}"
                )

            with right:
                st.write("")
                if st.button(
                    "Register →",
                    key=f"workshop_{name}",
                    type="primary",
                    use_container_width=True
                ):
                    st.session_state.selected_workshop = name
                    navigate("Register")


# -------------------- REGISTRATION PAGE --------------------

def register_page():

    st.markdown("""
    <div class="hero">
        <span class="eyebrow">📝 JOIN A WORKSHOP</span>
        <h1>Start Your <span class="gradient-text">Journey.</span></h1>
        <p>
        Enter your details below to try our workshop registration process.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.registration:
        data = st.session_state.registration

        st.success("🎉 Demo registration completed successfully!")

        st.markdown("### 📋 Registration Summary")

        with st.container(border=True):
            st.write(f"**👤 Name:** {data['name']}")
            st.write(f"**📧 Email:** {data['email']}")
            st.write(f"**🏫 College:** {data['college']}")
            st.write(f"**📚 Workshop:** {data['workshop']}")

        st.info(
            "This is a demo only. Registration details are kept temporarily "
            "in the current app session and are not saved to a permanent database."
        )

        if st.button("➕ Try Another Registration", type="primary"):
            st.session_state.registration = None
            st.rerun()

        return

    st.markdown("### 👤 Participant Details")

    selected = st.session_state.selected_workshop
    names = list(WORKSHOPS.keys())
    selected_index = names.index(selected) if selected in names else 0

    with st.form("registration_form"):

        name = st.text_input(
            "Full Name *",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email Address *",
            placeholder="you@example.com"
        )

        college = st.text_input(
            "College / Institution *",
            placeholder="Enter your college name"
        )

        workshop = st.selectbox(
            "Select Workshop *",
            names,
            index=selected_index
        )

        confirmed = st.checkbox(
            "I understand that this is a demonstration registration form."
        )

        submitted = st.form_submit_button(
            "Submit Registration  →",
            type="primary",
            use_container_width=True
        )

        if submitted:

            if not name.strip() or not email.strip() or not college.strip():
                st.error("Please complete all required fields.")

            elif not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                email.strip()
            ):
                st.error("Please enter a valid email address.")

            elif not confirmed:
                st.warning("Please confirm that you understand this is a demo.")

            else:
                st.session_state.registration = {
                    "name": name.strip(),
                    "email": email.strip(),
                    "college": college.strip(),
                    "workshop": workshop
                }
                st.rerun()

    st.caption(
        "* Required fields. This demo does not permanently save your details."
    )


# -------------------- CHATBOT PAGE --------------------

def assistant_page():

    st.markdown("""
    <div class="hero">
        <span class="eyebrow">🤖 WORKSHOP SUPPORT</span>
        <h1>Meet Your <span class="gradient-text">Assistant.</span></h1>
        <p>
        Ask about workshop topics, duration, registration and other
        frequently asked questions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.messages:

        st.markdown("### 👋 Hello! How can I help you?")

        suggestions = [
            "📚 What workshops are available?",
            "🐍 Tell me about Python",
            "📝 How do I register?",
            "🕒 What are the workshop durations?",
            "🎓 Are certificates available?",
            "💰 What are the workshop fees?"
        ]

        suggestion_cols = st.columns(2)

        for i, suggestion in enumerate(suggestions):
            with suggestion_cols[i % 2]:
                if st.button(
                    suggestion,
                    key=f"question_{i}",
                    use_container_width=True
                ):
                    st.session_state.pending_question = suggestion
                    st.rerun()

    def answer_question(question):

        q = question.lower()

        if any(x in q for x in ["hello", "hi", "hey", "namaste"]):
            return (
                "Hello! 👋 Welcome to WorkshopHub. "
                "I can help you explore workshops, check durations "
                "and understand the registration process."
            )

        if "workshop" in q or "available" in q or "list" in q:
            return (
                "📚 **Our Featured Workshops**\n\n"
                "- 🐍 Python Programming — 2 days\n"
                "- 🤖 Artificial Intelligence — 3 days\n"
                "- 💻 Web Development — 2 days\n"
                "- 🔐 Cyber Security — 2 days\n\n"
                "Visit the Workshops page to explore them."
            )

        if "python" in q:
            return (
                "🐍 **Python Programming**\n\n"
                "Learn variables, loops, functions and problem-solving.\n\n"
                "**Duration:** 2 days\n\n"
                "**Level:** Beginner"
            )

        if "artificial intelligence" in q or re.search(r"\bai\b", q):
            return (
                "🤖 **Artificial Intelligence**\n\n"
                "Explore AI fundamentals, intelligent systems and "
                "real-world applications.\n\n"
                "**Duration:** 3 days"
            )

        if "web" in q or "website" in q:
            return (
                "💻 **Web Development**\n\n"
                "Explore HTML, CSS and JavaScript and learn how "
                "modern websites are built.\n\n"
                "**Duration:** 2 days"
            )

        if "cyber" in q or "security" in q:
            return (
                "🔐 **Cyber Security**\n\n"
                "Learn about online safety, digital threats and "
                "cybersecurity fundamentals.\n\n"
                "**Duration:** 2 days"
            )

        if "register" in q or "registration" in q or "sign up" in q:
            return (
                "📝 To try registering:\n\n"
                "1. Open the **Register** page using the top navigation.\n"
                "2. Enter your name, email and college.\n"
                "3. Choose a workshop.\n"
                "4. Confirm the demo notice and submit.\n\n"
                "Note: This demo does not save details to a permanent database."
            )

        if "duration" in q or "long" in q or "days" in q:
            return (
                "🕒 **Workshop Durations**\n\n"
                "- Python Programming: 2 days\n"
                "- Artificial Intelligence: 3 days\n"
                "- Web Development: 2 days\n"
                "- Cyber Security: 2 days"
            )

        if "certificate" in q:
            return (
                "🎓 Certificate availability has not been configured "
                "for this demo. Please confirm certificate details "
                "with the actual workshop organiser."
            )

        if "fee" in q or "price" in q or "cost" in q:
            return (
                "💰 Workshop fees have not been configured in this demo. "
                "Please contact the workshop organiser for confirmed pricing."
            )

        if "thank" in q:
            return "You're welcome! 😊 Feel free to ask another question."

        return (
            "I can help you with workshops, duration, registration, "
            "certificates and fees.\n\n"
            "Try asking: **Tell me about Python** or "
            "**How do I register?**\n\n"
            "_I'm a rule-based demo assistant that uses predefined answers._"
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    pending = st.session_state.pending_question
    st.session_state.pending_question = None

    user_input = st.chat_input("💬 Ask me about workshops...")

    question = pending or user_input

    if question:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        response = answer_question(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()

    if st.session_state.messages:
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            st.rerun()


# -------------------- PAGE ROUTER --------------------

current_page = st.session_state.page

if current_page == "Home":
    home_page()

elif current_page == "Workshops":
    workshops_page()

elif current_page == "Assistant":
    assistant_page()

elif current_page == "Register":
    register_page()

else:
    home_page()

# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
    <strong>🎓 WorkshopHub</strong><br>
    Discover skills. Build your future.<br>
    Academic Demonstration Project · 2026
</div>
""", unsafe_allow_html=True)
