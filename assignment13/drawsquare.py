import arcade

SPACING = 20
MARGIN = 110

arcade.open_window(400, 400, "Square of diamonds")

arcade.set_background_color(arcade.color.AMARANTH_PINK)

arcade.start_render()

for row in range(10):
    for column in range(10):
        if (row%2==0 and column%2==0) or (row%2==1 and column%2==1):
            x = column * SPACING + MARGIN
            y = row * SPACING + MARGIN

            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.LEMON,45)
        elif (row%2==0 and column%2==1) or (row%2==1 and column%2==0):
            x = column * SPACING + MARGIN
            y = row * SPACING + MARGIN

            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.GREEN_YELLOW,45)


arcade.finish_render()

arcade.run()
