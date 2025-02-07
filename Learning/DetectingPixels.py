import tkinter as tk
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
                
                # Check if the pixel matches the target color
                if pixel_color == target_color:
                    print(f"Pixel found at ({x}, {y}) with color {pixel_color}")
                    img_copy.putpixel((x, y), (0, 255, 0))  # Mark found pixel with green
                else:
                    img_copy.putpixel((x, y), (255, 255, 255))  # Restore original color

# Create the main window
root = tk.Tk()
root.title("Pixel Detection Visualizer")

def on_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        label.config(text="Processing...")
        target_color = (255, 0, 0)  # RGB color to detect (e.g., red)
        
        # Define maximum dimensions for the scaled image
        max_width = 400
        max_height = 400
        
        detect_pixel(file_path, target_color, image_label, max_width, max_height)
        label.config(text="Processing complete.")

# Create a label for status messages
label = tk.Label(root, text="No file selected", bg="black", fg="white")
label.pack()

# Create a label to display the image
image_label = tk.Label(root, bg="black")
image_label.pack()

# Create a button to select the image
button = tk.Button(root, text="Choose file", command=on_button_click, bg="green", fg="white")
button.pack(side=tk.BOTTOM)

# Run the application
root.configure(bg="black")  # Set background color to black
root.geometry("500x500")  # Set initial window size
root.mainloop()
