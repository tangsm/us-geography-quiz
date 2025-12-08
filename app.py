import streamlit as st
import random
import time

# ==========================================
# 1. PAGE CONFIGURATION & RUMI STYLE
# ==========================================
st.set_page_config(
    page_title="10 in a row!",
    page_icon="🌀",
    layout="centered"
)

# Custom CSS for "Rumi Style" (Elegant, Gold, Calligraphy)
st.markdown(
    """
    <style>
    /* --- MAIN TITLE & QUOTE --- */
    .rumi-header {
        font-family: 'Zapfino', 'Brush Script MT', cursive; 
        color: #D4AC0D; /* Gold */
        text-shadow: 3px 3px 5px #1A5276; /* Deep Teal Shadow */
        text-align: center;
        font-size: 110px; /* Huge Title */
        line-height: 1.2;
        margin-bottom: 10px;
        padding-bottom: 0px;
    }
    .rumi-sub {
        font-family: 'Garamond', serif;
        color: #1A5276; /* Deep Teal */
        text-align: center;
        font-size: 35px; /* Huge Quote */
        font-style: italic;
        line-height: 1.4;
        margin-bottom: 30px;
    }
    
    /* --- MATH QUESTION --- */
    .big-math {
        font-size: 100px; 
        font-weight: bold; 
        color: #D4AC0D; /* Gold numbers */
        text-shadow: 2px 2px 2px #000000;
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Courier New', monospace;
    }

    /* --- SIDEBAR STYLING --- */
    [data-testid="stSidebar"] {
        background-color: #F9F9F9;
        border-right: 2px solid #D4AC0D;
    }
    /* Sidebar Headers */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        font-family: 'Zapfino', 'Brush Script MT', cursive !important;
        color: #D4AC0D !important;
        font-size: 35px !important;
        text-align: center;
    }
    /* Sidebar Text & Radio Buttons */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stRadio {
        font-family: 'Garamond', serif !important;
        color: #1A5276 !important;
        font-size: 20px !important;
        font-weight: bold;
    }

    /* --- BUTTON STYLING (THE ANSWERS) --- */
    div.stButton > button {
        font-size: 32px !important; /* BIGGER ANSWER TEXT */
        font-family: 'Garamond', serif !important;
        font-weight: bold !important;
        height: 80px !important; /* Taller buttons */
        width: 100%;
        color: #1A5276 !important; /* Deep Teal Text */
        background-color: #FEF9E7 !important; /* Parchment Background */
        border: 2px solid #D4AC0D !important; /* Gold Border */
        border-radius: 10px !important;
        transition: all 0.3s ease;
    }
    
    /* Hover Effect for Buttons */
    div.stButton > button:hover {
        transform: scale(1.02);
        background-color: #D4AC0D !important;
        color: white !important;
        border-color: #1A5276 !important;
    }
    
    /* Adjusting the progress bar color */
    .stProgress > div > div > div > div {
        background-color: #D4AC0D;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. HELPER FUNCTIONS
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
        
        wrong1 = correct_answer + random.randint(1, 5)
        wrong2 = correct_answer - random.randint(1, 5)
        wrong3 = (num1 + 1) * num2 
        
    # --- EXPONENTS (Super Powers) ---
    elif category == "Exponents (Super Powers) 🌀":
        base = random.randint(2, 10)
        exponent = 2 
        question = f"{base}²"
        correct_answer = base ** exponent
        explanation = f"{base}² means {base} × {base}, which equals {correct_answer}."
        
        wrong1 = base * 2          
        wrong2 = base + 2          
        wrong3 = (base + 1) ** 2   
        
    # --- ADDITION CHALLENGE ---
    elif category == "Big Addition ➕":
        num1 = random.randint(50, 400)
        num2 = random.randint(50, 400)
        question = f"{num1} + {num2} = ?"
        correct_answer = num1 + num2
        explanation = f"{num1} plus {num2} equals {correct_answer}."
        
        wrong1 = correct_answer + 10
        wrong2 = correct_answer - 10
        wrong3 = correct_answer + random.choice([-1, 1, -2, 2])

    options = list({correct_answer, wrong1, wrong2, wrong3})
    while len(options) < 4:
        options.append(correct_answer + random.randint(5, 20))
    
    random.shuffle(options)
    
    return {
        "question": question,
        "options": options,
        "answer": correct_answer,
        "explanation": explanation
    }

def reset_game():
    st.session_state.score = 0
    st.session_state.question_count = 0
    st.session_state.game_over = False
    st.session_state.current_problem = generate_problem(st.session_state.game_category)

# ==========================================
# 3. APP STATE MANAGEMENT
# ==========================================

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'game_category' not in st.session_state:
    st.session_state.game_category = "Multiplication ✖️"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# ==========================================
# 4. UI HEADER (RUMI STYLE)
# ==========================================

# Rumi Style Header with increased sizing
st.markdown('<p class="rumi-header">10 in a row!</p>', unsafe_allow_html=True)
st.markdown('<p class="rumi-sub">"Raise your words, not your voice. It is rain that grows flowers, not thunder."</p>', unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    new_category = st.radio(
        "Choose your Path:",
        ("Multiplication ✖️", "Exponents (Super Powers) 🌀", "Big Addition ➕")
    )
    
    if new_category != st.session_state.game_category:
        st.session_state.game_category = new_category
        reset_game()
        st.rerun()

    st.divider()
    if st.button("🔄 Start New Journey"):
        reset_game()
        st.rerun()

# Initialize Game
if st.session_state.current_problem is None:
    st.session_state.current_problem = generate_problem(st.session_state.game_category)

# ==========================================
# 5. GAME LOGIC & SCREEN
# ==========================================

if st.session_state.game_over:
    # --- SCORE REPORT ---
    final_score = st.session_state.score
    percentage = int((final_score / 10) * 100)
    
    # Rumi-themed Feedback
    if percentage == 100:
        st.balloons()
        st.markdown(f"<h1 style='text-align: center; color: #D4AC0D;'>🌟 Perfect! 🌟</h1>", unsafe_allow_html=True)
        st.success("You have found the treasure within! (100%)")
    elif percentage >= 80:
        st.markdown(f"<h1 style='text-align: center; color: #1A5276;'>Excellent!</h1>", unsafe_allow_html=True)
        st.info("You are very close to the stars! Keep climbing.")
    else:
        st.markdown(f"<h1 style='text-align: center; color: #C0392B;'>Good Journey!</h1>", unsafe_allow_html=True)
        st.warning("Mistakes are just steps on the path of learning.")
        
    st.metric(label="Final Score", value=f"{percentage}%", delta=f"{final_score}/10")
    
    st.divider()
    if st.button("Play Again (New Questions)", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

else:
    # --- ACTIVE GAME ---
    problem = st.session_state.current_problem
    q_num = st.session_state.question_count + 1
    
    st.write(f"**Step {q_num} of 10**")
    st.progress(st.session_state.question_count / 10)
    
    # Big Math Display
    st.markdown(f'<div class="big-math">{problem["question"]}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    options = problem['options']
    
    for i, option in enumerate(options):
        col = col1 if i % 2 == 0 else col2
        if col.button(str(option), use_container_width=True, key=f"btn_{i}"):
            
            # Check Answer
            if option == problem['answer']:
                st.session_state.score += 1
                st.toast(f"✅ Correct! {problem['explanation']}", icon="🌟")
            else:
                st.toast(f"❌ Not quite. The answer was {problem['answer']}.", icon="🌀")
                time.sleep(1)
            
            # Next Question Logic
            st.session_state.question_count += 1
            if st.session_state.question_count >= 10:
                st.session_state.game_over = True
            else:
                st.session_state.current_problem = generate_problem(st.session_state.game_category)
            
            st.rerun()

    st.divider()
    
    if st.session_state.game_category == "Exponents (Super Powers) 🌀":
        with st.expander("ℹ️ The Secret of the Square"):
            st.write(f"Remember: **{problem['question'][0]}²** is not adding. It is multiplying the number by itself.")
