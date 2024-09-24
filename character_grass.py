from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90

def draw():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)


# while(True)

for i in range(0,1):
    while(x<=760):
        draw()
        x = x+20
        delay(0.01)

    while(y<=560):
        draw()
        y = y+20
        delay(0.01)

    while(x>=30):
        draw()
        x = x-20
        delay(0.01)

    while(y>90):
        draw()
        y = y-20
        delay(0.01)

    while(x<400):
        draw()
        x = x+20
        delay(0.01)


close_canvas()
