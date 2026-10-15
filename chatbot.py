import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Workshop Chatbot", page_icon="🎓")

st.title("🎓 Workshop Registration Chatbot")
st.write("Hello! Ask me about workshops or register below.")

workshops = [
    "Python Programming",
    "Artificial Intelligence and Machine Learning",
    "Web Development",
    "Cyber Security"
]

question = st.chat_input("Ask me something...")

if question:
    st.chat_message("user").write(question)

    q = question.lower()

    if "workshop" in q or "available" in q:
        answer = "Available workshops:\n" + "\n".join(
            f"{i+1}. {w}" for i, w in enumerate(workshops)
        )
    elif "python" in q:
        answer = "Python Programming teaches Python basics and programming."
    elif "artificial intelligence" in q or "ai" in q:
        answer = "The AI/ML workshop introduces artificial intelligence and machine learning."
    elif "web" in q:
        answer = "The Web Development workshop introduces website development."
    elif "cyber" in q:
        answer = "The Cyber Security workshop introduces online safety and security."
    elif "register" in q or "registration" in q:
        answer = "Please fill in the registration form below!"
    elif "hello" in q or "hi" in q:
        answer = "Hello! 😊 Welcome to the Workshop Registration Assistant."
    else:
        answer = (
            "I can help with Python, AI/ML, Web Development, "
            "Cyber Security, and workshop registration. "
            "Please ask me about one of these topics."
        )

    st.chat_message("assistant").write(answer)

st.divider()
st.header("📝 Workshop Registration")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    workshop = st.selectbox("Choose a Workshop", workshops)

    submitted = st.form_submit_button("Register")

    if submitted:
        if not name.strip() or not email.strip() or "@" not in email:
            st.error("Please enter a valid name and email.")
        else:
            file = "registrations.csv"

            data = pd.DataFrame([{
                "Name": name,
                "Email": email,
                "Workshop": workshop,
                "Date": datetime.now().strftime("%Y-%m-%d")
            }])

            if os.path.exists(file):
                data.to_csv(file, mode="a", header=False, index=False)
            else:
                data.to_csv(file, index=False)

            st.success("Registration completed successfully!")
