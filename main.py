import tkinter
from tkinter import Tk, IntVar
import random as rn
from tkinter import Label, PhotoImage
from objects import Snake, Apple
from logic import SnakeLogic
import time

win = Tk()
win.geometry("500x500")
win.resizable(False, False)
game_frame = tkinter.Frame(win)
game_frame.pack(fill='both', expand=True)
game_field = tkinter.Frame(game_frame)
game_field.pack(fill='both', expand=True)

score_var = IntVar()
score_var.set(0)
score_lbl = Label(game_frame, textvariable=score_var, font=("A nic", "24"))
score_lbl.place(x=10, y=0)

loc_tuple1 = (250, 400)
head = Snake.SnakePart(1, 10, loc_tuple1, r"graphic\snake.png", game_field)
second_part = Snake.SnakePart(1, 10, (loc_tuple1[0], loc_tuple1[1] + 10), r"graphic\snake.png", game_field)
third_part = Snake.SnakePart(1, 10, (loc_tuple1[0], loc_tuple1[1] + 20), r"graphic\snake.png", game_field)
snake_parts = [head, second_part, third_part]


start_direction = "up"
direction = start_direction


def change_direction_to_right(e):
    global direction
    if direction != "left":
        direction = "right"


win.bind("d", change_direction_to_right)


def change_direction_to_up(e):
    global direction
    if direction != "down":
        direction = "up"


win.bind("w", change_direction_to_up)


def change_direction_to_down(e):
    global direction
    if direction != "up":
        direction = "down"


win.bind("s", change_direction_to_down)


def change_direction_to_left(e):
    global direction
    if direction != "right":
        direction = "left"


win.bind("a", change_direction_to_left)


one_time_ticket = False


def add_part():
    global one_time_ticket
    one_time_ticket = True


loc = (rn.randrange(0, 500, 10), rn.randrange(0, 500, 10))
apple = Apple.Apple(loc, r"graphic\apple.png", game_field)
apple.render()

game_over = False
while not game_over:
    win.after(50)

    if direction == "up":
        SnakeLogic.move_up_head(snake_parts, Snake, game_field)
    elif direction == "right":
        SnakeLogic.move_right_head(snake_parts, Snake, game_field)
    elif direction == "down":
        SnakeLogic.move_down_head(snake_parts, Snake, game_field)
    elif direction == "left":
        SnakeLogic.move_left_head(snake_parts, Snake, game_field)

    for another_part in snake_parts:
        if snake_parts.index(another_part) == 0:
            pass
        elif snake_parts[0].loc_tuple == another_part.loc_tuple:
            game_over = True
            break

    if snake_parts[0].loc_tuple == apple.loc_tuple:
        add_part()
        score_var.set(score_var.get()+1)
        t = (rn.randrange(0, 500, 10), rn.randrange(0, 500, 10))
        apple.loc_tuple = t

    if one_time_ticket:
        one_time_ticket = False
    else:
        snake_parts.pop(-1)

    SnakeLogic.forget_all(game_field)
    SnakeLogic.render_apple(apple, game_field)
    SnakeLogic.render_snake(snake_parts, master=game_field)
    head_loc = snake_parts[0].loc_tuple
    if (0 > head_loc[0] or head_loc[0] > game_frame.winfo_width()) or (0 > head_loc[1] or head_loc[1] >
                                                                       game_frame.winfo_height()):
        game_over = True




win.mainloop()
