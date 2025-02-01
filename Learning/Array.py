import tkinter as tk

# Create array to store the list
array = []

def is_empty():
    return textbox.get() == ""

def on_button_click(event=None):
    if is_empty():
        print("Empty")
    else:
        array.append(textbox.get())
        if checkbtn_check.get() == 1:
            array.sort()
            print("Sorted")
        else:
            print("Not sorted")

        label.config(text="Array: " + str(array))
        textbox.delete(0 ,tk.END) # Clear the textbox

# Create the main window
root = tk.Tk()
root.title("Simple UI")

# Create a label
label = tk.Label(root, text="Add to your list")
label.pack()

# Create a textbox
textbox = tk.Entry(root)
textbox.pack(padx=5, pady=5)
# Bind the Enter key to the on_button_click function
textbox.bind("<Return>", on_button_click)

# Create a button
button = tk.Button(root, text="Add and refresh", command=on_button_click)
button.pack()

# Create a radiobutton
checkbtn_check = tk.IntVar()
checkbtn = tk.Checkbutton(root, text="Sort", variable=checkbtn_check)
checkbtn.pack(padx=5, pady=5)

# Run the application
root.geometry("300x200")
root.mainloop()
