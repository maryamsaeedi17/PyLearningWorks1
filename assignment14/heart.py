import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__("heart.png")
        self.center_x = 30*x
        self.center_y = 20
        self.width = 35
        self.height = 30