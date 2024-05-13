# Noah Meissner 11.05.2024
from tkinter import *
from PIL import ImageTk
from Filter.Contrast import Contrast
from Filter.Brightness import Brightness
from Filter.Threshold import Threshold
from Filter.Blur import Blur
from Filter.Sharpness import Sharpness
from Filter.Erode import Erode
from Filter.Dilate import Dilate
from Filter.Swirl import Swirl
import tkinter as tk
from tkinter import filedialog
import PIL
from enum import Enum
import PIL.Image
import PIL.ImageTk


# Enum to clarify which filter are implemented
class Filter(Enum):
    Threshold = 1
    Brightness = 2
    Contrast = 3
    Blur = 4
    Sharpness = 5
    Erode = 6
    Dilate = 7
    Swirl = 8


# Open Scale Window to get factor for image Filter
def open_scale(factors):
    root_slider = tk.Toplevel()
    root_slider.geometry("200x100")
    root_slider.title("Select Value")

    scale_value = tk.DoubleVar(value=(factors[0] + factors[1]) / 2)

    def update_value(value):
        scale_value.set(value)

    scale = tk.Scale(
        root_slider,
        from_=factors[0],
        to=factors[1],
        resolution=0.2,
        orient='horizontal',
        command=update_value)
    scale.pack()

    root_slider.wait_window()
    print(scale_value.get())
    return scale_value.get()


# Shows About Window


def open_about():
    top = Toplevel()
    top.title("About")
    msg = Label(top, text="Programmed by © Noah Meissner")
    msg.pack(fill='x', padx=50, pady=20)


"""
Class creates graphical interface to apply image filters
"""


class GraphicalInterface:
    def __init__(self, terminal_image=None):
        # Declare variables
        self.point_start = None
        self.point_end = None
        self.final_img = None
        self.root = Tk(className='Image Processor')
        self.root.geometry("800x600")
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Dropdown-Menu File"
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=lambda: self.open_image())
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=lambda: self.save_picture())
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Dropdown-Menu "Edit"
        edit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(
            label="Define Area",
            command=lambda: self.define_area())

        # Dropdown-Menu "Filter"
        filter_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Filter", menu=filter_menu)
        filter_menu.add_command(
            label="Threshold",
            command=lambda: self.apply_filter(Filter.Threshold))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Brightness",
            command=lambda: self.apply_filter(Filter.Brightness))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Contrast",
            command=lambda: self.apply_filter(Filter.Contrast))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Blur",
            command=lambda: self.apply_filter(Filter.Blur))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Sharpen",
            command=lambda: self.apply_filter(Filter.Sharpness))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Erode",
            command=lambda: self.apply_filter(Filter.Erode))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Dilate",
            command=lambda: self.apply_filter(Filter.Dilate))
        filter_menu.add_separator()
        filter_menu.add_command(
            label="Swirl",
            command=lambda: self.apply_filter(Filter.Swirl))
        filter_menu.add_separator()

        # Dropdown-Menu "Help"
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=open_about)
        frame_image = Frame(self.root, borderwidth=2, relief=RAISED)
        frame_image.pack(fill=BOTH, expand=True)
        self.label_image = Label(frame_image)
        self.label_image.pack(fill=BOTH, expand=True)
        if terminal_image is not None:
            self.show_image(terminal_image)

        self.root.mainloop()

    # Method to apply filter on image
    def apply_filter(self, filter_chosen):
        if hasattr(self.label_image, 'original'):
            image = self.final_img
            if self.final_img is None:
                image = self.label_image.original
            match filter_chosen:
                case Filter.Threshold:
                    filter_object = Threshold(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Brightness:
                    filter_object = Brightness(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Contrast:
                    filter_object = Contrast(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Sharpness:
                    filter_object = Sharpness(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Blur:
                    filter_object = Blur(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Erode:
                    filter_object = Erode(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Dilate:
                    filter_object = Dilate(
                        image,
                        self.point_start,
                        self.point_end)
                case Filter.Swirl:
                    filter_object = Swirl(
                        image,
                        self.point_start,
                        self.point_end)
                case _:
                    filter_object = None
                    print("Unknown Filter")
        if filter_object is not None:
            value = open_scale(filter_object.get_slider_information())
            self.final_img = filter_object.process(value)
            tk_image = ImageTk.PhotoImage(self.final_img)
            self.label_image.config(image=tk_image)
            self.label_image.image = tk_image

    # Method to define specific area in the image to apply filters there
    def define_area(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Parameter Input")
        dialog.geometry("300x200")
        labels = ['x_min', 'y_min', 'x_max', 'y_max']
        entries = {}
        for i, label in enumerate(labels):
            tk.Label(dialog, text=f"{label}:").grid(row=i, column=0)
            entry = tk.Entry(dialog)
            entry.grid(row=i, column=1, pady=5, padx=10)
            entries[label] = entry

        def submit():
            params = {key: item.get() for key, item in entries.items()}
            self.point_start = [int(params['x_min']), int(params['y_min'])]
            self.point_end = [int(params['x_max']), int(params['y_max'])]
            dialog.destroy()

        submit_button = tk.Button(dialog, text="Submit", command=submit)
        submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Save modified Picture
    def save_picture(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png"),
                       ("JPEG image", "*.jpg"),
                       ("All files", "*.*")])
        if file_path:
            if self.final_img is not None:
                self.final_img.save(file_path)

    # Open Image for editing
    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = PIL.Image.open(file_path)
            print(file_path)
            self.show_image(image)

    def show_image(self, received_image):
        if received_image is not None:
            width, height = received_image.size
            factor = width / height
            height_new = int(600 / factor)
            image = received_image.resize(
                (600, height_new),
                PIL.Image.Resampling.LANCZOS)
            self.final_img = image
            tk_image = ImageTk.PhotoImage(image)
            self.label_image.config(image=tk_image)
            self.label_image.image = tk_image
            self.label_image.original = image
        else:
            print("No image selected")


if __name__ == '__main__':
    # Start Interface
    interface = GraphicalInterface()
