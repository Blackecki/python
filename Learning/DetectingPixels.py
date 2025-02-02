#Work in progress
import tkinter as tk
from PIL import Image
from tkinter import filedialog

def detect_pixel(image_path, target_color):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode
        img = img.convert('RGB')
        width, height = img.size
        
        # Iterate over each pixel
        for x in range(width):
            for y in range(height):
                # Get the color of the pixel
                pixel_color = img.getpixel((x, y))
                # Check if the pixel matches the target color
                if pixel_color == target_color:
                    print(f"Pixel found at ({x}, {y}) with color {pixel_color}")

# Example usage
#image_path = 'path_to_your_image.jpg'
#target_color = (255, 0, 0)  # RGB color to detect (e.g., red)
#detect_pixel(image_path, target_color)

# Create the main window
root = tk.Tk()
root.title("Simple UI")

def on_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        label.config(text=f"Selected file: {file_path}")
        # Optionally, you can call detect_pixel here with the selected file
        # detect_pixel(file_path, target_color)

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack()

# Create a button
button = tk.Button(root, text="Choose file", command=on_button_click)
button.pack()

# Run the application
root.configure(bg="black")  # Set background color to black
root.mainloop()