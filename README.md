# JARVIS AI Assistant 🤖

JARVIS AI Assistant is an advanced conversational AI interface built with Streamlit and Google's Gemini AI. It provides a modern, interactive web interface for natural language interactions with context awareness and memory capabilities.

## Features ✨

- **Natural Language Processing**: Engage in human-like conversations with context awareness
- **Web Navigation**: Open websites through voice commands
- **Customizable Interface**: Choose between dark and light themes
- **Adjustable AI Personality**: Switch between Professional, Friendly, and Witty modes
- **Memory Retention**: Maintains conversation context for more coherent interactions
- **Real-time Weather & Time Awareness**: Provides contextual greetings based on time of day
- **Interactive Chat Interface**: Modern, animated UI with message history
- **System Statistics**: Monitor usage and performance metrics

## Prerequisites 📋

Before running the application, ensure you have:
- Python 3.7 or higher installed
- A Google API key for Gemini AI
- Internet connection for AI model access

## Installation 🚀

1. Clone the repository:
```bash
git clone [repository-url]
cd jarvis-ai-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment:
   - Create a `.streamlit/secrets.toml` file
   - Add your Google API key:
     ```toml
     [general]
     api_key = "your-api-key-here"
     ```

## Usage 💡

1. Start the application:
```bash
streamlit run app.py
```

2. Access the web interface through your browser (typically at `http://localhost:8501`)

3. Use the interface:
   - Type messages in the chat input
   - Use the sidebar to adjust settings
   - Monitor system statistics
   - Clear chat history as needed

### Basic Commands 📝

- Ask any question naturally
- "Open [website]" - Navigate to websites
- "Exit" or "Quit" - End the session

### Advanced Features 🔥

- **Context Awareness**: JARVIS remembers recent conversations for better responses
- **Time-Based Greetings**: Receives appropriate greetings based on time of day
- **Error Handling**: Graceful handling of connection and processing issues
- **Responsive Design**: Works on both desktop and mobile devices

## Customization ⚙️

### Settings Available:
- **Theme**: Choose between Dark and Light modes
- **AI Personality**: Adjust between Professional, Friendly, and Witty
- **Language**: Interface supports multiple languages (English default)

## Technical Details 🔧

- Built with Streamlit for the front-end interface
- Integrates Google's Gemini AI for natural language processing
- Uses PyTZ for timezone management
- Implements Plotly for any data visualizations
- Features modern CSS animations and styling

## Error Handling 🚨

The application includes comprehensive error handling for:
- API connection issues
- Invalid user inputs
- Model processing errors
- Network connectivity problems

## Best Practices 📈

1. Be specific in your questions
2. Use natural language for better responses
3. Take advantage of context-aware features
4. Monitor system statistics for performance
5. Clear chat history periodically for optimal performance

## Security Considerations 🔐

- API keys are stored securely in Streamlit secrets
- User data is not permanently stored
- Session state is cleared upon browser refresh

## Limitations ⚠️

- Requires active internet connection
- API key must be valid for functionality
- Response time may vary based on network conditions
- Memory retention limited to current session

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

[Add your license information here]

## Support 📫

For support, please [add contact information or support channels]

---

**Note**: This project is for educational and demonstration purposes. Please ensure compliance with Google's Gemini AI usage terms and conditions.
