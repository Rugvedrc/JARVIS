# JARVIS AI Assistant

An advanced AI-powered chatbot built with Streamlit and Google's Gemini AI, featuring a sleek dark theme, context-aware conversations, and intelligent command processing.

## 🌟 Features

- **🤖 Advanced AI Conversations**: Powered by Google Gemini 1.5 Flash
- **🎨 Modern UI**: Beautiful dark theme with animations and gradient effects
- **🧠 Context-Aware**: Remembers recent conversation context
- **⏰ Time-Aware Greetings**: Personalized greetings based on time of day
- **🌐 Web Integration**: Open websites directly from chat
- **💾 Session Memory**: Retains conversation history during session
- **⚙️ Customizable Settings**: Adjust AI personality and theme
- **📊 System Statistics**: Track messages and memory usage

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Internet connection

## 🚀 Installation

1. **Clone or download this repository**

2. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `requirements.txt` file with the following dependencies:**

```
streamlit
google-generativeai
pillow
requests
pandas
plotly
pytz
```

## 🔧 Setup

### 1. Get Your Gemini API Key

- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Sign in with your Google account
- Create a new API key

### 2. Configure Streamlit Secrets

Create a `.streamlit/secrets.toml` file in your project directory:

```toml
[general]
api_key = "your-gemini-api-key-here"
```

**Project structure should look like:**
```
your-project/
├── .streamlit/
│   └── secrets.toml
├── app.py
├── requirements.txt
└── README.md
```

**⚠️ Security Note:** 
- Never commit your `secrets.toml` file to version control
- Add `.streamlit/` to your `.gitignore` file

## 💻 Usage

1. **Run the application:**

```bash
streamlit run app.py
```

(Replace `app.py` with your actual filename)

2. **Using JARVIS:**
   - Type your message in the chat input at the bottom
   - Ask questions, request information, or give commands
   - Use natural language for best results

## 🎯 Available Commands

### Basic Interactions
- **General Questions**: Ask anything!
  - "What is artificial intelligence?"
  - "Explain quantum computing"
  - "Tell me a joke"

### Web Navigation
- **Open Websites**: 
  - "Open Google"
  - "Go to YouTube"
  - "Visit GitHub"

### Session Control
- **Exit**: `exit`, `quit`, `bye`, `goodbye`

## ⚙️ Customization Options

### AI Personality Settings
Choose from three personality modes:
- **Professional**: Formal and business-like
- **Friendly**: Casual and approachable
- **Witty**: Humorous and clever

### Theme Options
- **Dark** (default): Easy on the eyes
- **Light**: Traditional bright theme

Access settings in the sidebar under "⚙️ Settings"

## 📁 Project Structure

```
├── app.py                    # Main application file
├── .streamlit/
│   └── secrets.toml         # API key configuration (create this)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔍 Key Features Explained

### Context Awareness
JARVIS remembers the last 5 messages to provide context-aware responses, making conversations feel more natural.

### Time-Aware Greetings
Greets you differently based on the time of day in Asia/Kolkata timezone:
- Morning (5 AM - 12 PM): "Good morning"
- Afternoon (12 PM - 5 PM): "Good afternoon"
- Evening (5 PM - 9 PM): "Good evening"
- Night (9 PM - 5 AM): "Good night"

### Session Memory
Stores conversation history and custom data during your session (resets on page refresh).

### System Statistics
Track your usage in real-time:
- Total messages sent
- Session start time
- Memory usage

## 🛠️ Troubleshooting

### API Key Issues
**Error: "Failed to initialize AI model"**
- Verify your API key in `.streamlit/secrets.toml`
- Ensure the file path and format are correct
- Check if you have API access in Google AI Studio

### Website Opening Issues
**Websites not opening:**
- Ensure you have a default web browser configured
- Check your firewall/security settings
- Try using full URLs (e.g., "Open https://google.com")

### Display Issues
**Chat not updating:**
- Refresh the page
- Clear browser cache
- Check browser console for errors

### Dependencies
**Import errors:**
```bash
pip install --upgrade -r requirements.txt
```

## 🔒 Security Best Practices

1. **Never commit API keys** to public repositories
2. **Use `.gitignore`** to exclude sensitive files:
   ```
   .streamlit/secrets.toml
   __pycache__/
   *.pyc
   ```
3. **Rotate API keys** periodically
4. **Monitor API usage** in Google AI Studio

## 🎨 Customization Guide

### Changing Colors
Edit the CSS in the `st.markdown()` section:
```python
background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
```

### Adding New Commands
Add to the `TASK_HANDLERS` dictionary:
```python
TASK_HANDLERS = {
    'your_command': lambda param: f"Response: {param}",
}
```

### Modifying AI Behavior
Adjust the context prompt in `process_command()`:
```python
context_prompt = f"""You are JARVIS, an advanced AI assistant. 
[Your custom instructions here]
"""
```

## 📊 System Requirements

- **RAM**: 2GB minimum, 4GB recommended
- **Storage**: 500MB for dependencies
- **Network**: Stable internet connection for API calls
- **Browser**: Modern browser (Chrome, Firefox, Edge, Safari)

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Image analysis capabilities
- [ ] File upload and analysis
- [ ] Calendar integration
- [ ] Task management system
- [ ] Export chat history
- [ ] Custom command creation
- [ ] Integration with external APIs

## 📝 Known Limitations

- Session data resets on page refresh
- API rate limits apply (Gemini free tier)
- Web opening requires default browser setup
- Context limited to last 5 messages

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Add new features
- Improve error handling
- Enhance UI/UX
- Optimize performance
- Add unit tests

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Acknowledgments

- **Streamlit**: Amazing framework for building data apps
- **Google Gemini**: Powerful AI model
- **Plotly**: Interactive charting library
- **Community**: For inspiration and support

## 📞 Support

For issues or questions:
- Check the [Streamlit Documentation](https://docs.streamlit.io/)
- Review [Gemini API Documentation](https://ai.google.dev/docs)
- Search existing issues or create a new one

## 🌟 Tips for Best Experience

1. **Be Specific**: Clear questions get better answers
2. **Use Context**: Follow-up questions work great
3. **Experiment**: Try different personality modes
4. **Natural Language**: Talk to JARVIS like a human
5. **Check Stats**: Monitor your usage in the sidebar

---

**Made with ❤️ using Streamlit and Google Gemini AI**

*JARVIS is ready to assist you!* 🤖✨
