from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('Circle')
    pass


def run_rectangle():
    print('Rectangle')
    pass


while (True):    
    run_rectangle()
    run_circle()
    break;
   
close_canvas()
