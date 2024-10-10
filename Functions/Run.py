import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyjokes  # Import pyjokes for telling jokes
from Functions.greet import greet_user
from Functions.talk import talk
from Functions.Take_command import take_command
from Functions.screenshot import take_screenshot
from Functions.application import open_application
from GUI.gui import run_gui  # Import the run_gui function

def run_jarvis():
    while True:  # Loop to keep listening for commands
        command = take_command()  # Take voice input
        if command is None:
            continue  # If no command is detected, continue to listen
        
        # Normalize the command to lowercase for consistent checking
        command = command.lower()

        if 'jarvis' in command:
        
            talk("Wake up key word detected...")
            greet_user()
            run_gui()  # Open the GUI when the command is detected
            continue  # Go back to listening for more commands

        # Handle other commands
        elif 'launch' in command:
            open_application(command)
            talk(f"Application {command} launched.")

        elif 'open youtube' in command:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            talk("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in command:
            talk("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif 'open linkedin' in command:
            talk("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")

        elif 'search google for' in command:
            search_query = command.replace('search google for', '')
            talk(f"Searching Google for {search_query}")
            pywhatkit.search(search_query)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")

        elif 'tell me about' in command:
            topic = command.replace('tell me about', '')
            info = wikipedia.summary(topic, 1)
            talk(info)

        elif 'screenshot' in command:
            talk("What should be the file name for the screenshot?")
            file_name = take_command()  # Take voice input for the screenshot name
            if file_name:
                take_screenshot(file_name)

        elif 'joke' in command:  # Add this line for jokes
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'exit' in command or 'stop' in command:
            talk("Closing JARVIS... Take care!")
            break  # Exit the loop to stop JARVIS
        
        else:
            talk("Sorry, I didn't understand that. Please try again.")
