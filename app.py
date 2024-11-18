import streamlit as st
import google.generativeai as genai
import datetime
import webbrowser
import json
from PIL import Image
import requests
import io
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import pytz
from datetime import datetime, timedelta

api_key = st.secrets["general"]["api_key"]

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'context' not in st.session_state:
    st.session_state.context = []
if 'memory' not in st.session_state:
    st.session_state.memory = {}
if 'settings' not in st.session_state:
    st.session_state.settings = {
        'theme': 'dark',
        'language': 'English',
        'personality': 'Professional'
    }

# Configure page with theme
st.set_page_config(
    page_title="Enhanced JARVIS AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with animations and modern design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: #FFFFFF;
        font-family: 'Roboto', sans-serif;
    }
    
    .stChatMessage {
        background: rgba(46, 46, 46, 0.7);
        backdrop-filter: blur(10px);
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeIn 0.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(62, 62, 62, 0.8);
        color: white;
        border-radius: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 0.5rem 1rem;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border-radius: 0.5rem;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    
    .sidebar .sidebar-content {
        background: rgba(30, 30, 30, 0.9);
    }
    
    .chart-container {
        background: rgba(46, 46, 46, 0.7);
        border-radius: 1rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 5px;
    }
    
    .status-online {
        background-color: #4CAF50;
        box-shadow: 0 0 10px #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Configure Gemini AI with safety settings
@st.cache_resource
def setup_gemini():
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

# Enhanced greeting with weather and time awareness
timezone=pytz.timezone('Asia/Kolkata')
def get_enhanced_greeting():
    current_time = datetime.now(timezone)
    hour = current_time.hour
    weather_conditions = ["clear", "cloudy", "rainy", "sunny"]
    current_weather = random.choice(weather_conditions)
    
    formatted_time = current_time.strftime("%I:%M %p")
    
    if 5 <= hour < 12:
        time_greeting = "Good morning"
    elif 12 <= hour < 17:
        time_greeting = "Good afternoon"
    elif 17 <= hour < 21:
        time_greeting = "Good evening"
    else:
        time_greeting = "Good night"
    
    return f"{time_greeting}! I'm JARVIS, your advanced AI assistant. It's currently {formatted_time}."

# Task categories and handlers
TASK_HANDLERS = {
    'search': lambda q: f"Searching for information about: {q}",
    'calculate': lambda expr: f"Result: {eval(expr) if expr.replace('.','').replace('-','').replace('+','').replace('*','').replace('/','').isdigit() else 'Invalid expression'}",
    'reminder': lambda msg: st.session_state.memory.update({'reminder': msg}) or f"Reminder set: {msg}",
    'analyze': lambda data: f"Analysis complete: {data}",
}

# Enhanced command processor with context awareness
def process_command(command, model):
    try:
        command = command.strip()
        
        st.session_state.context.append(command)
        if len(st.session_state.context) > 5:
            st.session_state.context.pop(0)
        
        with st.chat_message("user"):
            st.write(f"{command}\n")
        
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_placeholder.write("🤔 Processing your request...")
            
            if command.lower().startswith(('open', 'go to', 'visit')):
                website_prompt = f"Extract website URL from: {command}. Respond with ONLY the URL, nothing else."
                response = model.generate_content(website_prompt).text.strip()
                
                if not response.startswith(('http://', 'https://')):
                    response = 'https://' + response
                
                try:
                    webbrowser.open(response)
                    response = f"📱 Opening {response} in your browser..."
                except Exception as e:
                    response = "⚠️ Sorry, I couldn't open that website. Please check the URL."
            
            
            
            elif command.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                response = "👋 Goodbye! Have a great day!"
            
            else:
                context_prompt = f"""You are JARVIS, an advanced AI assistant. 
                Recent context: {' | '.join(st.session_state.context[-3:])}
                Current query: {command}
                Respond in a {st.session_state.settings['personality']} way """
                
                response = model.generate_content(context_prompt).text
            
            response_placeholder.markdown(response)
        
        current_time = datetime.now(timezone).strftime("%I:%M:%S %p")
        st.session_state.messages.append({"role": "user", "content": command, "timestamp": datetime.now(timezone).strftime("%H:%M:%S")})
        st.session_state.messages.append({"role": "assistant", "content": response, "timestamp": datetime.now(timezone).strftime("%H:%M:%S")})
        
        return response
    
    except Exception as e:
        error_message = f"🚫 Error: {str(e)}"
        with st.chat_message("assistant"):
            st.error(error_message)
        st.session_state.messages.append({"role": "assistant", "content": error_message})
        return error_message

def main():
    try:
        model = setup_gemini()
    except Exception as e:
        st.error("⚠️ Failed to initialize AI model. Please check your API key and internet connection.")
        return

    with st.sidebar:
        st.title("🌟 JARVIS Control Center")
        
        st.markdown("""
            <div style='display: flex; align-items: center;'>
                <div class='status-indicator status-online'></div>
                <span>JARVIS is Online</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        with st.expander("⚙️ Settings"):
            st.session_state.settings['theme'] = st.selectbox(
                "Theme",
                ["Dark", "Light"],
                index=0
            )
            st.session_state.settings['personality'] = st.select_slider(
                "AI Personality",
                options=["Professional", "Friendly", "Witty"],
                value="Professional"
            )
        
        with st.expander("📚 Commands & Features"):
            st.markdown("""
                ### Basic Commands
                - Ask any question
                - "Open [website]" - Visit websites
                
                ### Advanced Features
                - Context-aware responses
                - Memory retention
                
                ### Pro Tips
                - Be specific in questions
                - Use natural language
                - Try follow-up questions
            """)
        
        with st.expander("📊 System Stats"):
            current_time = datetime.now(timezone).strftime("%I:%M %p")
            st.markdown(f"""
                - Messages: {len(st.session_state.messages)}
                - Active Since: {datetime.now(timezone).strftime("%I:%M %p")}
                - Memory Usage: {len(str(st.session_state.memory))} bytes
            """)
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.session_state.context = []
            st.rerun()  # Updated from experimental_rerun()

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("🤖 JARVIS AI Assistant")
        
        if not st.session_state.messages:
            st.markdown(f"### {get_enhanced_greeting()}")
            st.markdown("---")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(f"{message['content']}\n")
    

    user_input = st.chat_input("💭 Type your message here...")
    if user_input and not st.session_state.processing:
        st.session_state.processing = True
        process_command(user_input, model)
        st.session_state.processing = False

if __name__ == "__main__":
    main()