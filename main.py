import shapegenerator as sg
import imagemaker as im
import math as mh
from random import randint

WIDTH = 700
HEIGHT = 700    

def CreateShapes(canvas):
    center = (WIDTH//2, HEIGHT//2)
    #sg.MakeRectangle(canvas, 200, 100, (100, 5))#WORKS!
    #sg.MakeCircle(canvas, (0, 0))#WORKS!
    #sg.MakeLine(canvas, (100,200), (50, 100))#probable works
    #sg.MakePolygon(canvas, (100,100), 50, 10)#ABSOLUTELY WORKS
    #sg.MakePolygon(canvas, (100, 100), 50, 1)
    #sg.MakeCircle(canvas, (250, 250), 250)
    #for i in range(30):
    #    sg.MakeHypotrochoid(canvas, center, 27-i, 27, 10, 16)
        #sg.MakeHypotrochoid(canvas, center, 9, 11, 5, 10+i)
    #for i in range(5):
        #sg.MakeMaurer(canvas, center, 2+i,4+i)

    #xRand = randint(3, 50)
    #yRand = randint(37, 200)
    #print("it is", xRand, yRand)
    #sg.MakeMaurer(canvas, center,xRand,yRand)

    #for i in range(15):
    #    sg.MakeHyperSpiral(canvas, center, 100+i*3, 6, 2-i//5)
    #for i in range(3, 83):
    #    sg.MakePolygon(canvas, (HEIGHT//2, WIDTH//2), i*3, i)
    #sg.MakeCochleoid(canvas, (center[0], 0), 300, 5)
    sg.MakeRorshack(canvas, center, randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), 100)

def OutlineCanvas(canvas):
    sg.MakeRectangle(canvas, WIDTH-1, HEIGHT-1, (0, 0))


def main():
    canvas = sg.MakeCanvas(WIDTH, HEIGHT)
    OutlineCanvas(canvas)
    CreateShapes(canvas)
    im.FormImage(canvas)

if __name__ == "__main__":
    main()