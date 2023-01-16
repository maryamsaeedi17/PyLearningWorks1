import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x=random.randint(0,w)
        self.center_y=h+24
        self.change_x=0
        self.change_y=-1
        self.width=40
        self.height=50
        self.angle=180
        self.speed=1
        

    def move(self):
        self.center_y-=self.speed