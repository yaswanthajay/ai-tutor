import streamlit as st
from utils.compare import compare_user_code
from utils.explain import generate_pseudocode
from utils.speak import speak

st.title("🧠 AI Code Tutor - Learn by Doing")

lang = st.selectbox("Select Language", ["Python"])
user_code = st.text_area("✍️ Write your Code")

if st.button("🚀 Analyze"):
    with open("examples/correct_code.py") as f:
        correct_code = f.read()

    diff = compare_user_code(user_code, correct_code)
    pseudo = generate_pseudocode(user_code)

    st.subheader("🔍 Difference with Correct Code")
    st.code(diff)

    st.subheader("🧾 Pseudocode")
    st.text(pseudo)

    st.subheader("🔈 Voice Explanation")
    st.audio("explanation.mp3")

    speak("Here is the explanation of your code.")
