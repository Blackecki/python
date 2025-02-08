import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog

def detect_pixel(image_path, target_color, label, max_width, max_height):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode
        img = img.convert('RGB')
        
        # Scale the image to fit within max_width and max_height while maintaining aspect ratio
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        width, height = img.size
        
        # Create a copy of the image to draw on
        img_copy = img.copy()
        img_tk = ImageTk.PhotoImage(img_copy)
        label.config(image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection
        
        detected_count = 0 
        count = 0
        
        # Iterate over each pixel
        for x in range(width):
            for y in range(height):
                # Get the color of the pixel
                pixel_color = img.getpixel((x, y))
                
                # Highlight the current pixel being checked
                img_copy.putpixel((x, y), (255, 255, 0))  # Highlight with yellow
                img_tk = ImageTk.PhotoImage(img_copy)
                label.config(image=img_tk)
                label.image = img_tk  # Update the reference
                root.update()  # Update the GUI
                
                count += 1
                labelcount.config(text=f"Scanned {count} pixels")

                # Check if the pixel matches the target color
                if pixel_color == target_color:
                    detected_count += 1
                    labeldetected.config(text=f"Detected: {detected_count} pixels")
                    img_copy.putpixel((x, y), (0, 255, 0))  # Mark found pixel with green
                else:
                    img_copy.putpixel((x, y), (255, 0, 0))  # Mark non-matching pixel with red
        return detected_count

# Create the main window
root = tk.Tk()
root.title("Pixel Detection Visualizer")

def HideInteractibles():
    checkbox.pack_forget()
    button.pack_forget()

def ShowInteractibles():
    checkbox.pack() 
    button.pack()

def on_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        label.config(text="Processing...")
        
        # Open color chooser dialog
        target_color = colorchooser.askcolor(title="Choose target color")[0]
        if target_color:
            target_color = tuple(map(int, target_color))  # Convert to RGB tuple
            labeldetected.config(text=f"No {target_color} pixels detected")
            
            # Define maximum dimensions for the scaled image
            if precise_mode.get():  # Use .get() to retrieve the value of the BooleanVar
                max_width = 400
                max_height = 400
            else:
                max_width = 200
                max_height = 200
                HideInteractibles()
            detected_count = detect_pixel(file_path, target_color, detecting_img, max_width, max_height)
            label.config(text=f"Processing complete")
            ShowInteractibles()
            original_img = Image.open(file_path)
            original_img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            normal_img_tk = ImageTk.PhotoImage(original_img)
            normal_img.config(image=normal_img_tk)
            normal_img.image = normal_img_tk  # Keep a reference to avoid garbage collection

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
title_label = tk.Label(title_bar, text="Pixel Detection Visualizer", bg="black", fg="white")
title_label.pack(side=tk.LEFT)

# Create a label for status messages
label = tk.Label(root, text="No file selected", bg="black", fg="white")
label.pack()

# Create a label to display the image
detecting_img = tk.Label(root, bg="black")
detecting_img.pack()

normal_img = tk.Label(root, bg="black")
normal_img.pack()

labelcount = tk.Label(root, text="", bg="black", fg="white")
labelcount.pack(side=tk.BOTTOM)

labeldetected = tk.Label(root, text="", bg="black", fg="white")
labeldetected.pack(side=tk.BOTTOM)

precise_mode = tk.BooleanVar()  # Create a BooleanVar for the checkbox
checkbox = tk.Checkbutton(root, text="Precise mode (slower)", variable=precise_mode, bg="black", fg="green")
checkbox.pack(side=tk.BOTTOM)

# Create a button to select the image
button = tk.Button(root, text="Choose file", command=on_button_click, bg="green", fg="white")
button.pack(side=tk.BOTTOM)

# Run the application
root.configure(bg="black")  # Set background color to black
root.geometry("600x600")  # Set initial window size
root.overrideredirect(True)  # Remove window decorations
root.attributes("-topmost", True)  # Always keep the window on top
root.mainloop()
