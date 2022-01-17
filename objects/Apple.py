from tkinter import Label
from tkinter import PhotoImage


class Apple:
    def __init__(self, loc_tuple, png_path, master):
        self.loc_tuple = loc_tuple
        self.master = master
        self.apple_img = PhotoImage(file=png_path)
        self.apple_graphic = Label(master, image=self.apple_img, bd=0)

    def render(self):
        self.apple_graphic.place(x=self.loc_tuple[0], y=self.loc_tuple[1])
