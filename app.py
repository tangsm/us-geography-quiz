import streamlit as st
import random

# ==========================================
# 1. HELPER FUNCTIONS
# ==========================================

def generate_problem(category):
    """Generates a random math problem based on the category."""
    
    # --- MULTIPLICATION (Tables 1-12) ---
    if category == "Multiplication ✖️":
        num1 = random.randint(2, 12)
        num2 = random.randint(2, 12)
        question = f"{num1} × {num2} = ?"
        correct_answer = num1 * num2
        explanation = f"{num1} groups of {num2} is {correct_answer}."
        
        # Generate generic wrong options
        wrong1 = correct_answer + random.randint(1, 5)
        wrong2 = correct_answer - random.randint(1, 5)
        wrong3 = (num1 + 1) * num2 
        
    # --- EXPONENTS (Introductory Squares) ---
    elif category == "Exponents (Super Powers) 🚀":
        # Keep base numbers small for 3rd graders (2 to 10)
        base = random.randint(2, 10)
        exponent = 2 # Keep it to 'squares' for this age group
        question = f"{base}² (What is {base} to the power of 2?)"
        correct_answer = base ** exponent
        explanation = f"{base}² means {base} × {base}, which equals {correct_answer}."
        
        # Common mistakes as distractors
        wrong1 = base * 2          # The most common mistake (adding instead of multiplying)
        wrong2 = base + 2          # Adding the exponent
        wrong3 = (base + 1) ** 2   # The next square up
        
    # --- ADDITION CHALLENGE (3-digit) ---
    elif category == "Big Addition ➕":
        num1 = random.randint(50, 400)
        num2 = random.randint(50, 400)
        question = f"{num1} + {num2} = ?"
        correct_answer = num1 + num2
        explanation = f"{num1} plus {num2} equals {correct_answer}."
        
        wrong1 = correct_answer + 10
        wrong2 = correct_answer - 10
        wrong3 = correct_answer + random.choice([-1, 1, -2, 2])

    # Ensure options are unique and shuffle them
    options = list({correct_answer, wrong1, wrong2, wrong3})
    # If duplicates resulted in fewer than 4 options, fill with randoms
    while len(options) < 4:
        options.append(correct_answer + random.randint(5, 20))
    
    random.shuffle(options)
    
    return {
        "question": question,
        "options": options,
        "answer": correct_answer,
        "explanation": explanation
    }

# ==========================================
# 2. APP STATE MANAGEMENT
# ==========================================

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'game_category' not in st.session_state:
    st.session_state.game_category = "Multiplication ✖️"

# ==========================================
# 3. UI LAYOUT
# ==========================================

st.title("🧮 Math Wizard Adventure")
st.markdown("Pick a mode and see how high you can get your streak!")

# Sidebar for Settings
with st.sidebar:
    st.header("⚙️ Game Settings")
    new_category = st.radio(
        "Choose your Challenge:",
        ("Multiplication ✖️", "Exponents (Super Powers) 🚀", "Big Addition ➕")
    )
    
    # If category changes, reset the question
    if new_category != st.session_state.game_category:
        st.session_state.game_category = new_category
        st.session_state.current_problem = None
        st.session_state.streak = 0
        st.session_state.score = 0
        st.rerun()

    st.divider()
    st.metric("🏆 Total Score", st.session_state.score)
    st.metric("🔥 Current Streak", st.session_state.streak)
    
    if st.button("Reset Game"):
        st.session_state.score = 0
        st.session_state.streak = 0
        st.session_state.current_problem = None
        st.rerun()

# Generate a new problem if one doesn't exist
if st.session_state.current_problem is None:
    st.session_state.current_problem = generate_problem(st.session_state.game_category)

problem = st.session_state.current_problem

# Display the Question Area
st.divider()
st.markdown(f"<h1 style='text-align: center; color: #4F8BF9;'>{problem['question']}</h1>", unsafe_allow_html=True)
st.divider()

# Option Buttons
col1, col2 = st.columns(2)

options = problem['options']

for i, option in enumerate(options):
    col = col1 if i % 2 == 0 else col2
    if col.button(str(option), use_container_width=True):
        if option == problem['answer']:
            # CORRECT ANSWER
            st.session_state.score += 10
            st.session_state.streak += 1
            st.toast(f"✅ Awesome! {problem['explanation']}", icon="🌟")
            st.balloons()
            # Generate new problem immediately
            st.session_state.current_problem = generate_problem(st.session_state.game_category)
            st.rerun()
        else:
            # WRONG ANSWER
            st.toast("❌ Oops! Try again.", icon="🤔")
            st.session_state.streak = 0 # Reset streak on wrong answer
            st.error(f"Not quite! The answer was {problem['answer']}. ({problem['explanation']})")
            
            # Button to next question
            if st.button("Next Question ➡️"):
                st.session_state.current_problem = generate_problem(st.session_state.game_category)
                st.rerun()

# Explainer text for Exponents (since it's hard for 3rd graders)
if st.session_state.game_category == "Exponents (Super Powers) 🚀":
    with st.expander("ℹ️ What is a 'Super Power' (Exponent)?"):
        st.write("""
        When you see a little number floating above another number (like **3²**), that is an **Exponent**. 
        
        It means you multiply the big number by itself!
        
        *   **2²** = 2 × 2 = 4
        *   **3²** = 3 × 3 = 9
        *   **4²** = 4 × 4 = 16
        """)
