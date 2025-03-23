import streamlit as st 
from gemini.Gemini import Gemini

st.title("Monogatari: Your AI-Powered Adventure")

# Initialize session state
if "setup_done" not in st.session_state:
    st.session_state.setup_done = False
if "chat" not in st.session_state:
    st.session_state.chat = []
# if "model" not in st.session_state:
#     st.session_state.model = Gemini()
#     st.session_state.model.init_chat(st.session_state.user_name,st.session_state.story_type, st.session_state.extra_instructions, st.session_state.plot_essentials)
#     st.toast("Model loaded!")

# 🎭 Story Setup Modal
if not st.session_state.setup_done:
    with st.form("story_setup"):
        st.subheader("Welcome, traveler! Let's set up your adventure.")
        
        # Get user inputs
        name = st.text_input("What's your name?")
        story_type = st.selectbox("What kind of story do you want?", ["Fantasy", "Sci-Fi", "Mystery", "Horror", "Post-Apocalyptic", "Medieval", "Surprise Me!"])
        extra_instructions = st.text_area("Any extra instructions for the AI?", placeholder="E.g., 'Make it dark and eerie' or 'Include magic.'")
        plot_essentials = st.text_area("Any must-have elements in your story?", placeholder="E.g., 'Include a dragon and a lost kingdom.'")
        
        start_btn = st.form_submit_button("Start Adventure!")

        if start_btn:
            st.session_state.user_name = name if name else "Traveler"
            st.session_state.story_type = story_type
            st.session_state.extra_instructions = extra_instructions
            st.session_state.plot_essentials = plot_essentials
            st.session_state.setup_done = True
            
            
            
            st.rerun()

# 📝 Story Intro (Only runs after setup)
if st.session_state.setup_done and len(st.session_state.chat) == 0:
  
    st.session_state.model = Gemini()
    st.session_state.model.init_chat(st.session_state.user_name,st.session_state.story_type, st.session_state.extra_instructions, st.session_state.plot_essentials)
    st.toast("Model loaded!")
  
    with st.status("Thinking..."): 
      intro = st.session_state.model.generate_start_message()  
    st.session_state.chat.append({"type": "bot", "message": intro})
    st.rerun()

# 🎭 Display chat messages
for item in st.session_state.chat:
    with st.chat_message(item['type']):
        st.write(item['message'])

# ✍️ Get user input
prompt = st.chat_input("Say something")

if prompt:
    st.session_state.chat.append({"type": "user", "message": prompt})
    st.rerun()

# 🤖 Generate AI response
if len(st.session_state.chat) > 0 and st.session_state.chat[-1]["type"] == "user":
    with st.status("Thinking..."):
        response = st.session_state.model.send_message(st.session_state.chat[-1]["message"])
    
    st.session_state.chat.append({"type": "bot", "message": response})
    st.rerun()
