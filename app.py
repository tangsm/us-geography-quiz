import streamlit as st
import random
import time

# ==========================================
# 1. PAGE CONFIGURATION & K-POP DEMON STYLE
# ==========================================
st.set_page_config(
    page_title="10 in a row!",
    page_icon="⚔️",
    layout="centered"
)

# Custom CSS for "K-Pop Demon Hunter" (Neon, Dark, Edgy)
st.markdown(
    """
    <style>
    /* Import futuristic font */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Teko:wght@600&display=swap');

    /* --- MAIN BACKGROUND --- */
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(315deg, #050505 0%, #1a0b2e 74%);
        color: #FFFFFF;
    }

    /* --- MAIN TITLE --- */
    .demon-header {
        font-family: 'Orbitron', sans-serif;
        color: #FF007F; /* Neon Pink */
        text-shadow: 0 0 10px #FF007F, 0 0 20px #FF007F, 0 0 40px #FF007F; /* Glowing Effect */
        text-align: center;
        font-size: 110px; /* Reverted to 110px */
        line-height: 1.1;
        margin-bottom: 10px;
        letter-spacing: 2px;
        font-style: italic;
        transform: skew(-10deg); /* Edgy slant */
    }

    /* --- SUBTITLE QUOTE --- */
    .demon-sub {
        font-family: 'Teko', sans-serif;
        color: #00F3FF; /* Electric Cyan */
        text-align: center;
        font-size: 35px; /* Reverted to 35px */
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 30px;
        text-shadow: 2px 2px #000000;
    }
    
    /* --- MATH QUESTION --- */
    .big-math {
        font-size: 110px; 
        font-weight: 900; 
        color: #FFFFFF;
        text-shadow: 4px 4px 0px #6600cc; /* Purple Shadow */
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Orbitron', sans-serif;
    }

    /* --- SIDEBAR STYLING --- */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #FF007F;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #FF007F !important;
        font-family: 'Orbitron', sans-serif !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stRadio {
        color: #00F3FF !important;
        font-family: 'Teko', sans-serif !important;
        font-size: 24px !important;
    }

    /* --- BUTTON STYLING (THE ANSWERS) --- */
    div.stButton > button {
        font-size: 35px !important;
        font-family: 'Orbitron', sans-serif !important;
        height: 90px !important;
        width: 100%;
        color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 2px solid #00F3FF !important; /* Cyan Border */
        border-radius: 0px !important; /* Sharp Edges for Demon Hunter look */
        transition: all 0.2s ease;
        text-transform: uppercase;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
    }
    
    /* Hover Effect for Buttons */
    div.stButton > button:hover {
        transform: scale(1.03) skew(-5deg); /* Dynamic movement */
        background-color: #FF007F !important; /* Pink on hover */
        border-color: #FFFFFF !important;
        box-shadow: 0 0 20px #FF007F;
    }
    
    /* Adjusting the progress bar color */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00F3FF, #FF007F);
    }
    
    /* Divider */
    hr {
        border-top: 2px solid #6600cc;
    }
    
    /* Toast/Alert overrides */
    div[data-baseweb="toast"] {
        background-color: #111;
        border: 1px solid #FF007F;
        color: #FFF;
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
        question = f"{num1} × {num2} = ?"
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
        question = f"{num1} + {num2} = ?"
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
# 4. UI HEADER (DEMON STYLE)
# ==========================================

st.markdown('<p class="demon-header">10 IN A ROW!</p>', unsafe_allow_html=True)
st.markdown('<p class="demon-sub">"SILENCE THE DOUBT. SLAY THE BEAT. HUNT THE ANSWERS."</p>', unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ MISSION SELECT")
    new_category = st.radio(
        "Choose Your Arena:",
        ("Combo Breaker (Multiplication)", "Limit Break (Exponents)", "Boss Raid (Big Addition)")
    )
    
    if new_category != st.session_state.game_category:
        st.session_state.game_category = new_category
        reset_game()
        st.rerun()

    st.divider()
    if st.button("🔄 RESPAWN (RESTART)"):
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
        st.markdown(f"<h1 style='text-align: center; color: #FF007F; font-family: Orbitron;'>⚔️ SSS RANK! ⚔️</h1>", unsafe_allow_html=True)
        st.success("MAXIMUM COMBO! YOU ARE UNSTOPPABLE! (100%)")
    elif percentage >= 80:
        st.markdown(f"<h1 style='text-align: center; color: #00F3FF; font-family: Orbitron;'>A RANK</h1>", unsafe_allow_html=True)
        st.info("Excellent hunting. You cleared the stage.")
    else:
        st.markdown(f"<h1 style='text-align: center; color: #FFFFFF; font-family: Orbitron;'>GAME OVER</h1>", unsafe_allow_html=True)
        st.warning("Your training isn't over. Respawn and try again.")
        
    st.metric(label="MISSION SCORE", value=f"{percentage}%", delta=f"{final_score}/10 Kills")
    
    st.divider()
    if st.button("PLAY AGAIN (NEW MISSION)", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

else:
    # --- ACTIVE GAME ---
    problem = st.session_state.current_problem
    q_num = st.session_state.question_count + 1
    
    st.write(f"**WAVE {q_num} / 10**")
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
                st.toast(f"🔥 CRITICAL HIT! {problem['explanation']}", icon="⚔️")
            else:
                st.toast(f"💀 MISS! The answer was {problem['answer']}.", icon="💢")
                time.sleep(1)
            
            # Next Question Logic
            st.session_state.question_count += 1
            if st.session_state.question_count >= 10:
                st.session_state.game_over = True
            else:
                st.session_state.current_problem = generate_problem(st.session_state.game_category)
            
            st.rerun()

    st.divider()
    
    if st.session_state.game_category == "Limit Break (Exponents)":
        with st.expander("ℹ️ TUTORIAL: POWER MOVES"):
            st.write(f"Remember: **{problem['question'][0]}²** means multiply the number by itself!")
