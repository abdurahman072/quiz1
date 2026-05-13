import streamlit as st

# 1. The 10 Mathematical Reasoning Questions
questions = [
    {"q": "What is the truth value of P ∨ ¬P?", "options": ["Tautology", "Contradiction", "Contingency"], "answer": "Tautology"},
    {"q": "If P is True and Q is False, what is P ∧ Q?", "options": ["True", "False"], "answer": "False"},
    {"q": "The contrapositive of P → Q is:", "options": ["Q → P", "¬Q → ¬P", "¬P → ¬Q"], "answer": "¬Q → ¬P"},
    {"q": "What is the negation of 'All students are smart'?", "options": ["No students are smart", "Some students are not smart", "All students are lazy"], "answer": "Some students are not smart"},
    {"q": "Which connective represents 'Exclusive OR'?", "options": ["∨", "⊕", "↔"], "answer": "⊕"},
    {"q": "If P is False, what is P → Q?", "options": ["Always True", "Always False", "Depends on Q"], "answer": "Always True"},
    {"q": "P ↔ Q is true only when:", "options": ["P is true", "Q is true", "P and Q have the same truth value"], "answer": "P and Q have the same truth value"},
    {"q": "What is the inverse of P → Q?", "options": ["¬P → ¬Q", "Q → P", "¬Q → ¬P"], "answer": "¬P → ¬Q"},
    {"q": "The statement ¬(P ∧ Q) is equivalent to:", "options": ["¬P ∧ ¬Q", "¬P ∨ ¬Q", "P ∨ Q"], "answer": "¬P ∨ ¬Q"},
    {"q": "A statement that is always false is called a:", "options": ["Tautology", "Fallacy", "Contradiction"], "answer": "Contradiction"}
]

st.set_page_config(page_title="AASTU Logic Quiz", page_icon="🎓")
st.title("AASTU Mathematical Reasoning Quiz 🎓")

# 2. Initialize Session State (The "Bookmark")
if 'idx' not in st.session_state:
    st.session_state.idx = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# 3. Game Logic
if st.session_state.idx < len(questions):
    item = questions[st.session_state.idx]
    
    st.subheader(f"Question {st.session_state.idx + 1} of {len(questions)}")
    st.write(item["q"])
    
    # Using a unique key for each question to prevent state clashing
    user_choice = st.radio("Select your answer:", item["options"], key=f"q_{st.session_state.idx}")
    
    if st.button("Check & Next"):
        if user_choice == item["answer"]:
            st.success("Correct! Well done.")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer was: {item['answer']}")
        
        st.session_state.idx += 1
        st.rerun()

else:
    st.balloons()
    st.header("Quiz Complete! 🎊")
    st.write(f"Your final score is **{st.session_state.score} / {len(questions)}**")
    
    if st.button("Restart Quiz"):
        st.session_state.idx = 0
        st.session_state.score = 0
        st.rerun()
