import streamlit as st
import random
import time

# ==========================================
# 1. PAGE CONFIGURATION & MOBILE OPTIMIZATION
# ==========================================
st.set_page_config(
    page_title="10 in a row!",
    page_icon="⚔️",
    layout="centered"
)

# Custom CSS for "K-Pop Demon Hunter" (Mobile Optimized)
st.markdown(
    """
    <style>
    /* Import futuristic font */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Teko:wght@500&display=swap');

    /* --- MOBILE OPTIMIZATION: REMOVE TOP PADDING --- */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* --- MAIN BACKGROUND --- */
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(315deg, #050505 0%, #1a0b2e 74%);
        color: #FFFFFF;
    }

    /* --- COMPACT TITLE --- */
    .demon-header {
        font-family: 'Orbitron', sans-serif;
        color: #FF007F; /* Neon Pink */
        text-shadow: 0 0 10px #FF007F;
        text-align: center;
        font-size: 40px; /* Smaller to fit phone screen */
        line-height: 1.1;
        margin-bottom: 5px;
        font-style: italic;
        transform: skew(-10deg);
    }

    /* --- COMPACT SUBTITLE --- */
    .demon-sub {
        font-family: 'Teko', sans-serif;
        color: #00F3FF; /* Electric Cyan */
        text-align: center;
        font-size: 18px; /* Smaller to save space */
        letter-spacing: 1px;
        margin-bottom: 10px;
        text-shadow: 1px 1px #000000;
    }
    
    /* --- MATH QUESTION (BIG BUT COMPACT) --- */
    .big-math {
        font-size: 70px; /* Still very easy to read */
        font-weight: 900; 
        color: #FFFFFF;
        text-shadow: 3px 3px 0px #6600cc;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 10px;
        font-family: 'Orbitron', sans-serif;
        line-height: 1;
    }

    /* --- SIDEBAR STYLING --- */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #FF007F;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
        color: #FF007F !important;
        font-family: 'Orbitron', sans-serif !important;
    }
    [data-testid="stSidebar"] .stRadio, [data-testid="stSidebar"] label {
        color: #00F3FF !important;
        font-family: 'Teko', sans-serif !important;
    }

    /* --- COMPACT BUTTONS (THE ANSWERS) --- */
    div.stButton > button {
        font-size: 30px !important; /* Large readable text */
        font-family: 'Orbitron', sans-serif !important;
        height: 65px !important; /* Shorter height to fit screen */
        width: 100%;
        color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 2px solid #00F3FF !important;
        border-radius: 4px !important;
        margin-bottom: 0px !important;
        transition: all 0.2s ease;
    }
    
    /* Hover Effect */
    div.stButton > button:hover {
        transform: scale(1.02);
        background-color: #FF007F !important;
        border-color: #FFFFFF !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00F3FF, #FF007F);
        height: 10px;
    }
    
    /* Hide the default hamburger menu to save space if desired (optional) */
    /* #MainMenu {visibility: hidden;} */
    /* footer {visibility: hidden;} */
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================

def generate_problem(category):
    """Generates a random math problem based on the category."""
    
    # --- MULTIPLICATION ---
    if category == "Combo Breaker (Multiplication)":
        num1 = random.randint(2, 12)
        num2 = random.randint(2, 12)
        question = f"{num1} × {num2}"
        correct_answer = num1 * num2
        explanation = f"{num1} hits of {num2} damage is {correct_answer}!"
        
        wrong1 = correct_answer + random.randint(1, 5)
        wrong2 = correct_answer - random.randint(1, 5)
        wrong3 = (num1 + 1) * num2 
        
    # --- EXPONENTS ---
    elif category == "Limit Break (Exponents)":
        base = random.randint(2, 10)
        exponent = 2 
        question = f"{base}²"
        correct_answer = base ** exponent
        explanation = f"{base}² is a power move: {base} × {base} = {correct_answer}!"
        
        wrong1 = base * 2          
        wrong2 = base + 2          
        wrong3 = (base + 1) ** 2   
        
    # --- ADDITION ---
    elif category == "Boss Raid (Big Addition)":
        num1 = random.randint(50, 400)
        num2 = random.randint(50, 400)
        question = f"{num1} + {num2}"
        correct_answer = num1 + num2
        explanation = f"Total HP recovered: {correct_answer}."
        
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
    st.session_state.game_category = "Combo Breaker (Multiplication)"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# ==========================================
# 4. UI HEADER (COMPACT)
# ==========================================

st.markdown('<p class="demon-header">10 IN A ROW!</p>', unsafe_allow_html=True)
st.markdown('<p class="demon-sub">SILENCE THE DOUBT. HUNT THE ANSWERS.</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ MISSION SELECT")
    new_category = st.radio(
        "Arena:",
        ("Combo Breaker (Multiplication)", "Limit Break (Exponents)", "Boss Raid (Big Addition)")
    )
    
    if new_category != st.session_state.game_category:
        st.session_state.game_category = new_category
        reset_game()
        st.rerun()

    st.divider()
    if st.button("🔄 RESPAWN"):
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
    
    # Demon-themed Feedback
    if percentage == 100:
        st.balloons()
        st.markdown(f"<h2 style='text-align: center; color: #FF007F; font-family: Orbitron;'>⚔️ SSS RANK! ⚔️</h2>", unsafe_allow_html=True)
        st.success("MAXIMUM COMBO! (100%)")
    elif percentage >= 80:
        st.markdown(f"<h2 style='text-align: center; color: #00F3FF; font-family: Orbitron;'>A RANK</h2>", unsafe_allow_html=True)
        st.info("Excellent hunting.")
    else:
        st.markdown(f"<h2 style='text-align: center; color: #FFFFFF; font-family: Orbitron;'>GAME OVER</h2>", unsafe_allow_html=True)
        st.warning("Respawn and try again.")
        
    st.metric(label="SCORE", value=f"{percentage}%", delta=f"{final_score}/10")
    
    st.divider()
    if st.button("PLAY AGAIN", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

else:
    # --- ACTIVE GAME ---
    problem = st.session_state.current_problem
    q_num = st.session_state.question_count + 1
    
    # Compact Progress
    st.progress(st.session_state.question_count / 10)
    st.caption(f"WAVE {q_num} / 10")
    
    # Big Math Display
    st.markdown(f'<div class="big-math">{problem["question"]}</div>', unsafe_allow_html=True)
    
    # Options grid
    col1, col2 = st.columns(2)
    options = problem['options']
    
    for i, option in enumerate(options):
        col = col1 if i % 2 == 0 else col2
        if col.button(str(option), use_container_width=True, key=f"btn_{i}"):
            
            # Check Answer
            if option == problem['answer']:
                st.session_state.score += 1
                st.toast(f"🔥 HIT!", icon="⚔️")
            else:
                st.toast(f"💀 MISS! Ans: {problem['answer']}", icon="💢")
                time.sleep(0.5)
            
            # Next Question Logic
            st.session_state.question_count += 1
            if st.session_state.question_count >= 10:
                st.session_state.game_over = True
            else:
                st.session_state.current_problem = generate_problem(st.session_state.game_category)
            
            st.rerun()
