
# Dot Counter Application

This application allows users to select an image, count green dots (or other colored objects), display the processed image with contours around the dots, and save the processed image. It is built using Python with OpenCV for image processing, Tkinter for the GUI, and PIL for image handling.

## Features

- **Select Image**: Users can select an image from their computer using a file dialog.
- **Count Dots**: The program detects and counts green dots (or other colored objects) based on their color in the image.
- **Display Processed Image**: The processed image, with contours drawn around detected dots, is displayed in the GUI.
- **Save Processed Image**: Users can save the processed image with contours to their computer.

## Prerequisites

You need to have the following Python packages installed:

- `opencv-python`
- `numpy`
- `Pillow` (PIL fork)
- `tkinter` (typically included with standard Python distributions)

You can install the required packages using the following command:

```bash
pip install opencv-python numpy Pillow
```

## How to Use

1. **Run the program**:
   Execute the Python script from your terminal or IDE.

   ```bash
   python dot_counter.py
   ```

2. **Select an Image**:
   Click the **"Select Image"** button to open a file dialog and choose an image to process.

3. **Process the Image**:
   The program will detect and count green dots in the image, display the processed image with contours, and show the dot count.

4. **Save the Processed Image**:
   After processing, click the **"Save Image"** button to save the processed image to your computer.

## Color Detection

This program detects objects based on their color. By default, it detects green dots using the HSV color range for green. You can adjust the color range in the `count_dots()` function by modifying the `lower_green` and `upper_green` values.

Example:

```python
lower_green = np.array([40, 50, 50])  # Adjust for lower bound of the desired color
upper_green = np.array([80, 255, 255])  # Adjust for upper bound of the desired color
```

## Known Issues

- The application may not detect non-green objects by default. Adjust the HSV values in the code to detect different colors.
- Large images may take longer to process. The program resizes large images to fit within the display canvas for better visibility.

## License

This project is open-source and free to use. No specific license applies.
"# dot-counter" 
