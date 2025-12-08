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

    /* --- FIX: INCREASE TOP PADDING SO TITLE ISN'T CUT OFF --- */
    .block-container {
        padding-top: 3rem !important; 
        padding-bottom: 1rem !important;
    }

    /* --- MAIN BACKGROUND --- */
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(315deg, #050505 0%, #1a0b2e 74%);
        color: #FFFFFF;
    }

    /* --- BIG TITLE --- */
    .demon-header {
        font-family: 'Orbitron', sans-serif;
        color: #FF007F; /* Neon Pink */
        text-shadow: 0 0 15px #FF007F, 3px 3px 0px #000000; /* Glow + Shadow */
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        line-height: 1.2; 
        margin-bottom: 5px;
        font-style: italic;
        transform: skew(-10deg);
        letter-spacing: -2px;
        padding-top: 10px; 
        white-space: nowrap;
    }

    /* --- SUBTITLE --- */
    .demon-sub {
        font-family: 'Teko', sans-serif;
        color: #00F3FF; /* Electric Cyan */
        text-align: center;
        font-size: 20px; 
        letter-spacing: 2px;
        margin-bottom: 15px;
        text-shadow: 1px 1px #000000;
        text-transform: uppercase;
    }
    
    /* --- MATH QUESTION --- */
    .big-math {
        font-size: 70px; 
        font-weight: 900; 
        color: #FFFFFF;
        text-shadow: 4px 4px 0px #6600cc;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 15px;
        font-family: 'Orbitron', sans-serif;
        line-height: 1;
    }

    /* --- CUSTOM STATS BOXES (High Visibility) --- */
    .stat-container {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stat-box {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        width: 48%;
    }
    .stat-label {
        font-family: 'Teko', sans-serif;
        color: #AAAAAA;
        font-size: 20px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .stat-value-pink {
        font-family: 'Orbitron', sans-serif;
        color: #FF007F; /* Neon Pink */
        font-size: 45px;
        font-weight: 900;
        text-shadow: 0 0 10px #FF007F;
    }
    .stat-value-cyan {
        font-family: 'Orbitron', sans-serif;
        color: #00F3FF; /* Cyan */
        font-size: 45px;
        font-weight: 900;
        text-shadow: 0 0 10px #00F3FF;
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
        font-size: 30px !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 65px !important;
        width: 100%;
        color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 2px solid #00F3FF !important;
        border-radius: 4px !important;
        margin-bottom: 0px !important;
        transition: all 0.2s ease;
    }
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
    st.session_state.start_time = time.time()
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
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# ==========================================
# 4. UI HEADER
# ==========================================

st.markdown('<div class="demon-header">10 IN A ROW!</div>', unsafe_allow_html=True)
st.markdown('<div class="demon-sub">SILENCE THE DOUBT. HUNT THE ANSWERS.</div>', unsafe_allow_html=True)

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
    # --- CALCULATE TIME ---
    end_time = time.time()
    total_time = end_time - st.session_state.start_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    time_str = f"{minutes}m {seconds}s" if minutes > 0 else f"{seconds}s"

    # --- SCORE REPORT ---
    final_score = st.session_state.score
    percentage = int((final_score / 10) * 100)
    
    # Demon-themed Feedback with Encouragement
    if percentage == 100:
        st.balloons()
        st.markdown(f"<h2 style='text-align: center; color: #FF007F; font-family: Orbitron;'>⚔️ SSS RANK! ⚔️</h2>", unsafe_allow_html=True)
        st.success(f"MAXIMUM COMBO! (100%)")
    elif percentage >= 80:
        st.markdown(f"<h2 style='text-align: center; color: #00F3FF; font-family: Orbitron;'>A RANK</h2>", unsafe_allow_html=True)
        st.info(f"Excellent hunting.")
    else:
        # --- NEW ENCOURAGING MESSAGE ---
        st.markdown(f"<h2 style='text-align: center; color: #FFFFFF; font-family: Orbitron;'>GAME OVER</h2>", unsafe_allow_html=True)
        st.warning("Mistakes are part of learning. Do you want to play again?")
    
    # --- CUSTOM HTML STATS DISPLAY (Colorful & Prominent) ---
    st.markdown(
        f"""
        <div class="stat-container">
            <div class="stat-box">
                <div class="stat-label">Mission Score</div>
                <div class="stat-value-pink">{percentage}%</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Clear Time</div>
                <div class="stat-value-cyan">{time_str}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    if st.button("PLAY AGAIN", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

else:
    # --- ACTIVE GAME ---
    problem = st.session_state.current_problem
    q_num = st.session_state.question_count + 1
    
    # Calculate current running time
    current_elapsed = int(time.time() - st.session_state.start_time)
    
    # Compact Progress & Info
    st.progress(st.session_state.question_count / 10)
    
    # Small stats row
    col_info1, col_info2 = st.columns([1,1])
    with col_info1:
        st.caption(f"WAVE {q_num} / 10")
    with col_info2:
        st.caption(f"⏱️ {current_elapsed}s") 
    
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
