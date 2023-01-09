import random
import math
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snow"


class Snowman(arcade.Sprite):
    def __init__(self,game):
        super().__init__("snowman.png")
        self.center_x=game.width // 2
        self.center_y=game.height//6
        self.width=80
        self.height=100
        self.speed=8


class Fire(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("fire.png")
        self.center_x=random.randint(0,w)
        self.center_y=h+24
        self.width=40
        self.height=40
        self.angle=180
        self.speed=4
        self.angle=0
        self.rotate=math.pi



class Snowflake:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_WIDTH)



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.snowflake_list = None
        self.me=Snowman(self)
        self.enemy=Fire(self.width,self.height)

    def start_snowfall(self):
        self.snowflake_list = []

        for i in range(50):
            snowflake = Snowflake()
            snowflake.x = random.randrange(SCREEN_WIDTH)
            snowflake.y = random.randrange(SCREEN_HEIGHT + 200)

            snowflake.size = random.randrange(4)
            snowflake.speed = random.randrange(20, 40)
            snowflake.angle = random.uniform(math.pi, math.pi * 2)

            self.snowflake_list.append(snowflake)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_CYAN)

    def on_draw(self):
        self.clear()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.WHITE)
        for snowflake in self.snowflake_list:
            arcade.draw_circle_filled(snowflake.x, snowflake.y,snowflake.size, arcade.color.WHITE)
        
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==97: # symbol A=97
            self.me.center_x-=self.me.speed
        elif symbol==100: # symbol D=100
            self.me.center_x+=self.me.speed


    def on_update(self, delta_time):
        self.enemy.center_y-=self.enemy.speed
        self.enemy.angle+=self.enemy.rotate
        
        for snowflake in self.snowflake_list:
            snowflake.y -= snowflake.speed * delta_time

            if snowflake.y < 0:
                snowflake.reset_pos()

            snowflake.x += snowflake.speed * math.cos(snowflake.angle) * delta_time
            snowflake.angle += 1 * delta_time



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.start_snowfall()
arcade.run()
