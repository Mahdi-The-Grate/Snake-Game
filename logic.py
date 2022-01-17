class SnakeLogic:
    @staticmethod
    def move_up_head(snake_parts, snake_obj, master):
        new_head = snake_obj.SnakePart(1, 10, (snake_parts[0].loc_tuple[0], snake_parts[0].loc_tuple[1] - 10),
                                       r"graphic\snake.png", master)
        snake_parts.insert(0, new_head)

    @staticmethod
    def move_right_head(snake_parts, snake_obj, master):
        new_head = snake_obj.SnakePart(1, 10, (snake_parts[0].loc_tuple[0] + 10, snake_parts[0].loc_tuple[1]),
                                       r"graphic\snake.png", master)

        snake_parts.insert(0, new_head)

    @staticmethod
    def move_down_head(snake_parts, snake_obj, master):
        new_head = snake_obj.SnakePart(1, 10, (snake_parts[0].loc_tuple[0], snake_parts[0].loc_tuple[1] + 10),
                                       r"graphic\snake.png", master)

        snake_parts.insert(0, new_head)

    @staticmethod
    def move_left_head(snake_parts, snake_obj, master):
        new_head = snake_obj.SnakePart(1, 10, (snake_parts[0].loc_tuple[0] - 10, snake_parts[0].loc_tuple[1]),
                                       r"graphic\snake.png", master)

        snake_parts.insert(0, new_head)

    @staticmethod
    def render_snake(snake_parts, master):
        for part in snake_parts:
            part.render()
        master.update()

    @staticmethod
    def render_apple(apple_obj, master):
        apple_obj.render()

    @staticmethod
    def forget_all(master):
        for widget in master.winfo_children():
            widget.place_forget()

