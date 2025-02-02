import tkinter as tk
from tkinter import messagebox # Import messagebox from tkinter

# Create array to store the list
array = []

def is_empty():
    return textbox.get() == ""

def on_button_click(event=None):
    if is_empty():
        print("Empty")
        messagebox.showwarning("Warning", "You didint put anything") # Show a warning message
    else:
        array.append(textbox.get())
        if checkbtn_check.get() == 1:
            array.sort()
            print("Sorted")
        else:
            print("Not sorted")

        label.config(text="Array: " + str(array))
        textbox.delete(0 ,tk.END) # Clear the textbox

def close_window():
    print("Closing window")
    root.destroy()

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_motion(event):
    x = (event.x_root - root.x)
    y = (event.y_root - root.y)
    root.geometry(f"+{x}+{y}")

# Create the main window
root = tk.Tk()
root.title("Simple UI")
root.configure(bg="black")  # Set background color to black
root.overrideredirect(True)  # Remove window decorations
root.attributes("-topmost", True)  # Always keep the window on top

# Create a frame for the title bar
title_bar = tk.Frame(root, bg="black", relief="raised", bd=2)
title_bar.pack(fill=tk.X)

# Bind the title bar to the move functions
root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", on_motion)

# Create close button
close_button = tk.Button(title_bar, text="X", command=close_window, bg="red", fg="white")
close_button.pack(side=tk.RIGHT)

# Create a title label
title_label = tk.Label(title_bar, text="Array testing and learning UI in python", bg="black", fg="white")
title_label.pack(side=tk.LEFT)

# Create a label
label = tk.Label(root, text="Add to your list", bg="black", fg="white")
label.pack()

# Create a textbox
textbox = tk.Entry(root)
textbox.pack(padx=5, pady=5)
# Bind the Enter key to the on_button_click function
textbox.bind("<Return>", on_button_click)

# Create a button
button = tk.Button(root, text="Add and refresh", command=on_button_click, bg="green", fg="white")
button.pack()

# Create a radiobutton
checkbtn_check = tk.IntVar()
checkbtn = tk.Checkbutton(root, text="Sort", variable=checkbtn_check, bg="green", fg="black")
checkbtn.pack(padx=5, pady=5)

# Run the application
root.geometry("300x200")
root.mainloop()
