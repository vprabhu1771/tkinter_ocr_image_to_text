import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Configure the path to tesseract.exe (if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pick_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg")]
    )
    if file_path:
        image = Image.open(file_path)
        '''
        In recent versions of the Pillow library, the ANTIALIAS constant has been deprecated and replaced by Resampling.LANCZOS
        '''
        # image = image.resize((200, 200), Image.ANTIALIAS)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)
        label_image.config(image=img)
        label_image.image = img

        # Convert image to text
        text = pytesseract.image_to_string(Image.open(file_path))
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text)

# Initialize the main window
root = tk.Tk()
root.title("OCR Image to Text")
root.geometry("500x300")

# Create the left frame for the Pick Image button
left_frame = tk.Frame(root, width=200, height=300)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Add a button to pick an image
pick_button = tk.Button(left_frame, text="Pick Image", command=pick_image)
pick_button.pack(pady=20)

# Add a label to display the image
label_image = tk.Label(left_frame)
label_image.pack()

# Create the right frame for the text area
right_frame = tk.Frame(root, width=300, height=300)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# Add a text area to display OCR result
text_area = tk.Text(right_frame, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
