import math

from pico2d import *

open_canvas()

#fill here
grass=load_image('grass.png')
character=load_image('character.png')
x=0
y=90

def run_rectagle():
    
    print("rectagle")

    #아랫쪽 무빙~
    for x in range(50,750,10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.02)
    pass

def run_circle():
    cx,cy,r=400,300,200
    for deg in range(0,360,5):
        x=cx+r*math.cos(deg/360*2*math.pi)
        y=cy+r*math.sin(deg/360*2*math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.02)

while (True):
    
    run_rectagle()
    #run_circle()
    break;
    

close_canvas()


