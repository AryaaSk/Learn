import tkinter as tk
from tkinter import messagebox
import json

# Create the main application window
root = tk.Tk()
root.title("Simple UI with Three Text Areas")

# Set the size of the window
root.geometry("1080x1080")

# Function to create a labeled text area with a button
def create_labeled_text_area_with_button(root, label_text, callback):
    # Create a frame to hold the label, text area, and button
    frame = tk.Frame(root)
    frame.pack(pady=10, fill='x')
    
    # Create and place the label
    label = tk.Label(frame, text=label_text, anchor='w')
    label.pack(fill='x')
    
    # Create and place the text area with a border
    text_area = tk.Text(frame, height=10, width=70, bd=2, relief="groove")
    text_area.pack(fill='x')
    
    if callback != None:
    # Button click event handler
        def on_button_click():
            content = text_area.get("1.0", tk.END).strip()
            if content:
                callback(root, content)
            else:
                messagebox.showwarning("Empty", f"{label_text} is empty!")

        # Create and place the button
        button = tk.Button(frame, text="Generate and Copy Prompt", command=on_button_click)
        button.pack(pady=5)
    
    return text_area

# Create labeled text areas with buttons
def GenerateInitialPrompt(root, prompt):
    generatedPrompt = f"What is {prompt}; output the response in markdown."
    root.clipboard_clear()
    root.clipboard_append(generatedPrompt)
    messagebox.showinfo("Copied", f"Prompt copied to clipboard!")
text_area1 = create_labeled_text_area_with_button(root, "Prompt", GenerateInitialPrompt)


def GenerateScriptPrompt(root, content):
    generatedPrompt = f"""
Split the following script into individual scenes with narration. Under each title and subtitle (marked with ## and ### respectively) please include scenes as a list: {content}. Return answer in JSON format provided by the Video interface given below.

interface Introduction {{
    title: string;
    narration: string;
}}

interface Scene {{
    title: string;
    subScenes: {{ subtitle: string, narration: string }}[];
}}

interface Summary {{
    narration: string;
}}

interface Video {{
    introduction: Introduction;
    scenes: Scene[];
    summary: Summary
}}

Content:
{content}
"""

    root.clipboard_clear()
    root.clipboard_append(generatedPrompt)
    messagebox.showinfo("Copied", f"Prompt copied to clipboard!")

text_area2 = create_labeled_text_area_with_button(root, "Content", GenerateScriptPrompt)


def ParseScript(root, script):
    #given the script as a JSON string, we will convert to an object
    #loop through each scene and generate video
    script = json.loads(script)
    scenes = script["scenes"]
    
    for scene in scenes:
        title = scene["title"]
        subScenes = scene["subScenes"]

        #each scene is an individual manim scene















text_area3 = create_labeled_text_area_with_button(root, "Script", ParseScript)



f = open("3script.json", "r")
script = f.read()
f.close()

ParseScript(root, script)








# Start the Tkinter event loop
#root.mainloop()
