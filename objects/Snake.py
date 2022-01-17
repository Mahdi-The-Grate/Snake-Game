from tkinter import Label
from tkinter import PhotoImage


class SnakePart:
    def __init__(self, length, speed, loc_tuple, png_path, master):
        self.length = length
        self.speed = speed
        self.loc_tuple = loc_tuple
        self.master = master
        self.snake_img = PhotoImage(file=png_path)
        self.snake_graphic = Label(master, image=self.snake_img, bd=0)

    def render(self):
        self.snake_graphic.place(x=self.loc_tuple[0], y=self.loc_tuple[1])

    def forget(self):
        self.snake_graphic.place_forget()

    def move_up(self):
        self.loc_tuple = (self.loc_tuple[0], self.loc_tuple[1] - 10)

    def move_down(self):
        self.loc_tuple = (self.loc_tuple[0], self.loc_tuple[1] + 10)

    def move_left(self):
        self.loc_tuple = (self.loc_tuple[0] - 10, self.loc_tuple[1])

    def move_right(self):
        self.loc_tuple = (self.loc_tuple[0] + 10, self.loc_tuple[1])