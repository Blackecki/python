import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog
import time

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
                    img_copy.putpixel((x, y), (255, 255, 255))  # Restore original color
        return detected_count

# Create the main window
root = tk.Tk()
root.title("Pixel Detection Visualizer")

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
            max_width = 200
            max_height = 200
            
            detected_count = detect_pixel(file_path, target_color, detecting_img, max_width, max_height)
            label.config(text=f"Processing complete")
            original_img = Image.open(file_path)
            original_img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            normal_img_tk = ImageTk.PhotoImage(original_img)
            normal_img.config(image=normal_img_tk)
            normal_img.image = normal_img_tk  # Keep a reference to avoid garbage collection

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

# Create a button to select the image
button = tk.Button(root, text="Choose file", command=on_button_click, bg="green", fg="white")
button.pack(side=tk.BOTTOM)

# Run the application
root.configure(bg="black")  # Set background color to black
root.geometry("500x500")  # Set initial window size
root.mainloop()
