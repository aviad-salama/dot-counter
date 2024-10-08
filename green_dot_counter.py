import cv2
import numpy as np
from tkinter import Tk, filedialog, Label, Button, Canvas
from PIL import Image, ImageTk


def count_dots(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if image is loaded successfully
    if image is None:
        raise Exception(f"Error: Could not load image from {image_path}")

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for green color (adjust as needed)
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # Create a mask for green pixels
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours (connected regions) in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the image (for visualization)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # Green color for contours

    # Count the number of contours (assuming each contour represents a dot)
    dot_count = len(contours)

    # Print the number of dots (for demonstration purposes)
    print(f"Number of dots: {dot_count}")

    return image, dot_count


def update_image(image, dot_count):
    # Resize image to fit canvas
    max_height = 480
    if image.shape[0] > max_height:
        scale = max_height / image.shape[0]
        width = int(image.shape[1] * scale)
        height = max_height
        image = cv2.resize(image, (width, height))

    # Convert the OpenCV image format to a format compatible with Tkinter
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    image_tk = ImageTk.PhotoImage(image=image_pil)

    # Update the image on the canvas
    image_canvas.image = image_tk  # Keep a reference to avoid garbage collection
    image_canvas.config(width=image_tk.width(), height=image_tk.height())  # Adjust canvas size
    image_canvas.create_image(0, 0, anchor='nw', image=image_tk)

    # Display dot count
    dot_count_label.config(text=f"Number of Dots: {dot_count}")

    # Store the processed image for saving later
    update_image.processed_image = image_rgb


def select_image():
    # Open a file selection dialog
    image_path = filedialog.askopenfilename()
    if image_path:
        try:
            image, dot_count = count_dots(image_path)
            update_image(image, dot_count)
        except Exception as e:
            print(f"Error: {e}")


def save_image():
    if hasattr(update_image, 'processed_image'):
        # Open a file dialog to select the save directory
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            try:
                # Convert processed image to PIL format and save
                pil_image = Image.fromarray(update_image.processed_image)
                pil_image.save(save_path)
                print(f"Saved processed image to {save_path}")
            except Exception as e:
                print(f"Error saving image: {e}")
    else:
        print("No processed image to save. Please process an image first.")


# Create the main window
window = Tk()
window.title("Dot Counter")

# Button to select image
select_button = Button(window, text="Select Image", command=select_image)
select_button.pack(pady=10)

# Button to save image
save_button = Button(window, text="Save Image", command=save_image)
save_button.pack(pady=10)

# Canvas to display the image
image_canvas = Canvas(window, width=640, height=480)
image_canvas.pack()

# Label to display dot count
dot_count_label = Label(window, text="")
dot_count_label.pack()

# Run the main loop
window.mainloop()
