# Created by mortza mansouri
# Free charge of use ...

import cv2 # for window
import tkinter as tk# for gui
from tkinter import filedialog # for picking file..

class ImageClickCoordinator:
  
    def __init__(self, root):
        self.root = root
        self.image = None
        self.coordinates_label = tk.Label(root, text="X: -, Y: -")
        self.coordinates_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.pack()

        self.x_label = tk.Label(root, text="X:")
        self.x_label.pack()
        self.x_entry = tk.Entry(root)
        self.x_entry.pack()

        self.y_label = tk.Label(root, text="Y:")
        self.y_label.pack()
        self.y_entry = tk.Entry(root)
        self.y_entry.pack()

        self.show_pointer_button = tk.Button(root, text="Show Pointer", command=self.show_pointer)
        self.show_pointer_button.pack()

        self.pointer_visible = False
        self.clicked_coordinates = None

    def select_image(self):
        file_path = filedialog.askopenfilename()
        self.image = cv2.imread(file_path)
        self.display_image()

    def display_image(self):
        cv2.imshow("Image", self.image)
        cv2.setMouseCallback("Image", self.on_mouse_click)

    def on_mouse_click(self, event, x, y):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.coordinates_label.config(text=f"X: {x}, Y: {y}")
            self.clicked_coordinates = (x, y)

    def show_pointer(self):
        x = int(self.x_entry.get())
        y = int(self.y_entry.get())
        if self.image is not None:
            cv2.circle(self.image, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Image", self.image)
            self.pointer_visible = True
        else:
            print("Please select an image first")

root = tk.Tk()
app = ImageClickCoordinator(root)
root.mainloop()
