import shapegenerator as sg
import imagemaker as im
import math as mh
from random import randint

WIDTH = 700
HEIGHT = 700

def RandomizeRorshack(canvas, center, max, size):
    a = randint(1,300)
    b = randint(1,300)
    c = randint(1,300)
    d = randint(1,300)
    print("making rorshack with",a,b,c,d)
    sg.MakeRorshack(canvas, center, a,b,c,d, max, size)

def CreateShapes(canvas):
    center = (WIDTH//2, HEIGHT//2)
    quarter = (WIDTH//4, HEIGHT//4)
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
    #sg.MakeMaurer(canvas, quarter,xRand,yRand)
    #sg.MakeMaurer(canvas, quarter,37,124)
    #sg.MakeMaurer(canvas, (center[0]//2,center[1]//2), 2, 127, 20)
    #for i in range(5):
    #    sg.MakeHyperSpiral(canvas, center, 50, 200)
    #for i in range(3, 83):
    #    sg.MakePolygon(canvas, (HEIGHT//2, WIDTH//2), i*3, i)
    #sg.MakeCochleoid(canvas, (center[0], 50), 300, 100, 5)
    #sg.MakeRorshack(canvas, center, 121, 121, 37, 37, 200, 200)
    #RandomizeRorshack(canvas, center, 200, 150)
    #sg.MakeRorshack(canvas, center, randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), 150)
    #sg.MakeLissajous(canvas, center, 3, 2)
    sg.MakeMystery(canvas, center, 50, 100)

def OutlineCanvas(canvas):
    sg.MakeRectangle(canvas, WIDTH-1, HEIGHT-1, (0, 0))


def main():
    canvas = sg.MakeCanvas(WIDTH, HEIGHT)
    OutlineCanvas(canvas)
    CreateShapes(canvas)
    im.FormImage(canvas)

if __name__ == "__main__":
    main()