import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=game.width // 2
        self.center_y=60
        self.width=40
        self.height=50
        self.speed=8


class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x=random.randint(0,w)
        self.center_y=h+24
        self.width=40
        self.height=50
        self.angle=180
        self.speed=4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=600,title="Spaceship🛸")
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self)
        self.doshman=Enemy(self.width,self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==97: # symbol A=97
            self.me.center_x-=self.me.speed
        elif symbol==100: # symbol D=100
            self.me.center_x+=self.me.speed

    def on_update(self, delta_time: float):
        self.doshman.center_y-=self.doshman.speed
    



window=Game()
arcade.run()

