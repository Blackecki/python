#I’m still having problems with my OS, and I can’t even import moviepy correctly. I’m fixing it right now and will continue this later.
#I just pasted the code from python/learning/CuteLittleUi as my starting point. I will work it up
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple UI")

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
