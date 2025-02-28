from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    boy.draw_now(x,y)
    delay(0.01)


def run_circle():
    print('CIRCLE')
    r,cx,cy = 300, 800//2, 600//2

    for degree in range(0,360,3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        draw_boy(x,y)
        
    pass

def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('RIGHT')
    for y in range(550,80,-10):
        draw_boy(790,y)
    pass

def run_bottom():
    print('BOTTOM')
    for x in range(800,0,-10):
        draw_boy(x,90)
    pass

def run_left():
    print('LEFT')
    for y in range(80,550,10):
        draw_boy(0,y)
    pass

def run_hypotenuse():
    print('HYPOTENUSE')
    y = 550
    for x in range(0,800,10):    
        y -= 550 // (800//10)
        draw_boy(x,y)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_triangle():
    print('TRIANGLE')
    run_bottom()
    run_left()
    run_hypotenuse()
    pass
    
while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
