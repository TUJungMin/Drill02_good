from pico2d import *

open_canvas()
x =400
y = 90
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('Circle')
    
   
    
    
   
    cx,cy,r = 400,300,200
    for deg in (0,360,5):
        clear_canvas_now()
        x = cx+r*math.cos(math.radians(deg))
        y = cy+r*math.sin(math.radians(deg))
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        delay(0.01)
   


def run_rectangle():
    print('Rectangle')
    pass


while (True):    
    run_rectangle()
    run_circle()
    break;
   

