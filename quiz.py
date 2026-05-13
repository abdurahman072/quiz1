import streamlit as st

# Set up the title
st.title("Ethiopia Quiz 🇪🇹")

# Initialize score in the app's memory
if 'score' not in st.session_state:
    st.session_state.score = 0

# Ask the question using a text input
user_answer = st.text_input("What is the capital of Ethiopia?")

# Create a button to submit
if st.button("Submit Answer"):
    if user_answer.lower() == "addis ababa":
        st.success("Correct! 🌟")
        st.session_state.score += 1
    else:
        st.error("Not quite. The capital is Addis Ababa. 📍")

# Show the score
st.write(f"### Current Score: {st.session_state.score}")