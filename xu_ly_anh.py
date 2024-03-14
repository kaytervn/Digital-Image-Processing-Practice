import tkinter as tk
import numpy as np
from tkinter.filedialog import Open
import cv2

L = 256


def Negative(imgin):
    imgout = L - 1 - imgin
    return imgout


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Xử lý ảnh")
        self.geometry("320x320")
        self.imgin = None
        self.imgout = None

        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(
            label="Open Image", command=self.mnu_file_open_image_click
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

        chapter3_menu = tk.Menu(menu, tearoff=0)
        chapter3_menu.add_command(label="Negative", command=self.mnu_c3_negative_click)
        menu.add_cascade(label="Chapter3", menu=chapter3_menu)
        self.config(menu=menu)

    def mnu_file_open_image_click(self):
        ftypes = [("Image", "*.jpg *.tif *.bmp *.gif *.png")]
        dlg = Open(self, filetypes=ftypes)
        filename = dlg.show()
        if filename != "":
            self.imgin = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            cv2.imshow("ImageIn", self.imgin)

    def mnu_c3_negative_click(self):
        self.imgout = Negative(self.imgin)
        cv2.imshow("Negative", self.imgout)


if __name__ == "__main__":
    app = App()
    app.mainloop()
