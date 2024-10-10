import tkinter as tk
from tkinter import Label, Button, Text, Scrollbar, messagebox
from PIL import Image, ImageTk, ImageSequence
import threading
import os
import sys
from Functions.talk import talk

# Preload GIFs to reduce delay
gif_paths = {
    "iron_man_loading": os.path.join("GIFs", "iron_man_loading.gif"),
    "circle_loading": os.path.join("GIFs", "circle_loading.gif"),
    "main_gui": os.path.join("GIFs", "main_gui.gif")
}

preloaded_gifs = {}
running = True  # Flag to manage application state

def preload_gif(gif_path, width, height):
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(img.resize((width, height), Image.Resampling.LANCZOS)) for img in ImageSequence.Iterator(gif)]
    return frames

def preload_gifs(width, height):
    for key, path in gif_paths.items():
        preloaded_gifs[key] = preload_gif(path, width, height)

# Function to display GIF once and sync with audio
def display_gif_once(label, gif_key, message=None, next_func=None):
    frames = preloaded_gifs[gif_key]
    
    # Clear label
    label.config(image='')

    # Start audio in a separate thread if there's a message
    if message:
        threading.Thread(target=talk, args=(message,)).start()

    def animate(frame_index):
        if frame_index < len(frames):
            label.config(image=frames[frame_index])
            label.image = frames[frame_index]  # Keep a reference
            label.after(30, animate, frame_index + 1)  # Reduced frame duration
        else:
            if next_func:
                next_func()  # Call next function after GIF ends

    animate(0)

# Function to display continuous GIF
def display_gif_continuous(label, gif_key):
    frames = preloaded_gifs[gif_key]
    
    def animate(frame_index):
        label.config(image=frames[frame_index % len(frames)])
        label.image = frames[frame_index % len(frames)]  # Keep a reference
        label.after(30, animate, frame_index + 1)  # Reduced frame duration

    animate(0)

# Redirect stdout to the Text widget for terminal-like functionality
class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.config(state=tk.DISABLED)

    def write(self, output):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, output)
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.see(tk.END)  # Auto-scroll to the bottom

    def flush(self):  # Necessary for Python stdout redirection
        pass

# Function to start listening for input
def start_listening():
    from Functions.Run import run_jarvis  # Import inside the function to avoid circular import
    threading.Thread(target=run_jarvis).start()

# Main GUI function
def run_gui():
    global running
    # Create main window and set to fullscreen
    root = tk.Tk()
    root.title("JARVIS GUI")
    root.attributes('-fullscreen', True)

    # Exit fullscreen with Escape key
    def exit_fullscreen(event=None):
        root.attributes('-fullscreen', False)

    root.bind("<Escape>", exit_fullscreen)

    global width, height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Preload GIFs with the screen size
    preload_gifs(width, height)

    # Load iron_man_loading.gif
    iron_man_label = Label(root)
    iron_man_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # Display iron man GIF
    threading.Thread(target=display_gif_once, args=(iron_man_label, "iron_man_loading",
                                                    "Initializing JARVIS... Activating all systems.",
                                                    lambda: display_gif_once(circle_loading_label, "circle_loading",
                                                    message="Checking for updates.... all devices are upto date...  System startup initialized .... system check complete ...all systems are operational", 
                                                    next_func=start_main_gui))).start()

    # Load circle_loading.gif
    circle_loading_label = Label(root)
    circle_loading_label.place(relx=0.5, rely=0.5, anchor="center")

    # Start main GUI
    def start_main_gui():
        iron_man_label.config(image='')
        circle_loading_label.config(image='')

        main_gui_label = Label(root)
        main_gui_label.place(relx=0.5, rely=0.5, anchor="center")
        display_gif_continuous(main_gui_label, "main_gui")  # Continuous GIF for main GUI

        # Terminal window in the top-right corner
        terminal_frame = tk.Frame(root)
        terminal_frame.place(relx=0.76, rely=0.02, relwidth=0.24, relheight=0.4)  # Adjust position to touch the right boundary

        # Text widget to act as terminal output
        terminal_text = Text(terminal_frame, wrap=tk.WORD, bg="black", fg="lime", font=("Consolas", 10))
        terminal_text.pack(expand=True, fill='both')

        # Redirect stdout to the Text widget
        sys.stdout = RedirectText(terminal_text)

        # Exit button
        exit_button = Button(root, text="Exit", command=exit_program, width=10, height=2, bg="#F44336", fg="white", font=('Arial', 12, 'bold'))
        exit_button.place(relx=0.95, rely=0.85, anchor="se")

        # Start button
        start_button = Button(root, text="Start", command=start_listening, width=10, height=2, bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'))
        start_button.place(relx=0.85, rely=0.85, anchor="se")  # Adjust position next to the exit button

    def exit_program():
        global running
        running = False  # Set the flag to false to indicate the GUI is closing
        root.quit()  # Stop the Tkinter main loop
        root.destroy()  # Close the window

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    run_gui()
