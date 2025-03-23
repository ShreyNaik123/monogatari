import streamlit as st

def render_header():
  st.markdown(
    """
    <style>
        /* Global styles */
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap');
        
        .main-container {
            background: linear-gradient(135deg, rgba(29, 53, 87, 0.8) 0%, rgba(20, 33, 61, 0.8) 100%);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 20px 0;
            backdrop-filter: blur(5px);
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Title styling */
        .title-container {
            margin-bottom: 25px;
            text-align: center;
        }
        
        .japanese-title {
            font-size: 60px;
            font-weight: bold;
            color: #FF6B6B;
            text-shadow: 0 0 10px rgba(255, 107, 107, 0.3);
            margin-bottom: 10px;
            letter-spacing: 2px;
        }
        
        .japanese-title ruby {
            font-size: 60px;
        }
        
        .japanese-title rt {
            font-size: 18px;
            color: #F1FAEE;
            opacity: 0.8;
        }
        
        .english-title {
            font-size: 42px;
            font-weight: bold;
            background: linear-gradient(90deg, #FF6B6B, #FFD166);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Nunito', sans-serif;
            margin-top: 5px;
            margin-bottom: 20px;
        }
        
        .subtitle {
            font-size: 22px;
            color: #A8DADC;
            font-family: 'Nunito', sans-serif;
            margin-bottom: 10px;
            line-height: 1.5;
        }
        
        /* Divider */
        .divider {
            height: 4px;
            background: linear-gradient(90deg, rgba(255,107,107,0.7), rgba(168,218,220,0.7));
            border-radius: 2px;
            margin: 20px 0;
            width: 100%;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #FF6B6B, #FF9E7A);
            color: white;
            font-weight: bold;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(255, 107, 107, 0.3);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 107, 107, 0.4);
        }
        
        /* Selectbox styling */
        .stSelectbox>div>div {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
st.markdown(
    """
    <div class="main-container">
        <div class="title-container">
            <div class="japanese-title">
                <ruby>Monogatari<rt>ものがたり</rt></ruby>
            </div>
            <div class="english-title">
                Your AI-Powered Adventure
            </div>
            <div class="subtitle">
                Embark on an interactive journey through worlds of imagination
            </div>
        </div>
        <div class="divider"></div>
    </div>
    """,
    unsafe_allow_html=True
)