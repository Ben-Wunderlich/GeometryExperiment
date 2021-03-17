import shapegenerator as sg
import imagemaker as im
import math as mh
from random import randint

WIDTH = 800
HEIGHT = 800

def RandomizeRorshack(canvas, center, max, size):
    a = randint(1,100)
    b = randint(1,100)
    c = randint(1,100)
    d = randint(1,100)
    print("making rorshack with",a,b,c,d)
    sg.MakeRorshack(canvas, center, a,b,c,d, max, size)

def PolygonChaos(canvas, center):
    sides = 5
    i = 0
    end=10
    while i <= end:
        sides = randint(3, 20)
        sg.MakePolygon(canvas, center, 50+i*10, sides)
        i+=1

def ChaosFlower(canvas, center, sizeStart = 20, times=7):
    i=0
    while i < times:
        seed1 = randint(7, 200)
        seed2 = randint(7, 201)
        print(seed1, seed2)
        sg.MakeMaurer(canvas, center, seed1, seed2, sizeStart+20*i)
        i+=1

def InscribedRandCircle(canvas, bigCenter, bigRadius=300, smallRadius=200, numInscribed=5):
    #outer circle
    sg.MakeCircle(canvas, bigCenter, bigRadius)
    possibleRadius = bigRadius - smallRadius
    for i in range(numInscribed):
        xPos = randint(-possibleRadius, possibleRadius)
        yFreedom = int(mh.sqrt((possibleRadius*possibleRadius) - (xPos*xPos)))
        yPos = randint(-yFreedom, yFreedom)
        sg.MakeCircle(canvas, (bigCenter[0]+xPos, bigCenter[1]+yPos), smallRadius)


def CreateShapes(canvas):
    center = (WIDTH//2, HEIGHT//2)
    quarter = (WIDTH//4, HEIGHT//4)
    threeQuarter = (center[0]+quarter[0], center[1]+quarter[1])
    #sg.MakeRectangle(canvas, 200, 100, (100, 5))#WORKS!
    #sg.MakeCircle(canvas, (0, 0))#WORKS!
    #sg.MakeLine(canvas, (100,200), (50, 100))#probable works
    #sg.MakePolygon(canvas, (100,100), 50, 6)#ABSOLUTELY WORKS

    #sg.MakeCircle(canvas, (250, 250), 250)
    #for i in range(30):
    #    sg.MakeHypotrochoid(canvas, center, 27-i, 27, 10, 16)
        #sg.MakeHypotrochoid(canvas, center, 9, 11, 5, 10+i)
    #for i in range(5):
        #sg.MakeMaurer(canvas, center, 2+i,4+i)

    #sg.MakeMaurer(canvas, quarter,200,7, 4)
    #for i in range(5):
    #    sg.MakeHyperSpiral(canvas, center, 50, 200)
    #sg.MakeHyperSpiral(canvas, center, 30, 80)
    #for i in range(3, 83):
    #    sg.MakePolygon(canvas, (HEIGHT//2, WIDTH//2), i*3, i)
    #sg.MakeCochleoid(canvas, (center[0], 50), 100, 100, 5)
    #sg.MakeRorshack(canvas, center, 121, 121, 37, 37, 200, 200)
    #sg.MakeRorshack(canvas, center, 1, 60, 1, 60, 200, 150)
    #sg.MakeRorshack(canvas, center, 200, 6, 101, 6, 200, 150)
    #RandomizeRorshack(canvas, center, 200, 150)
    #sg.MakeLissajous(canvas, center, 10, 11, 300)
    #PolygonChaos(canvas, center)
    #ChaosFlower(canvas, quarter)
    #InscribedRandCircle(canvas, center, 300, 200, 1)
    #sg.MakeNormalSpiral(canvas, center, 5, 200, 0.05, 0.2, True)



def OutlineCanvas(canvas):
    sg.MakeRectangle(canvas, WIDTH-1, HEIGHT-1, (0, 0))


def main():
    canvas = sg.MakeCanvas(WIDTH, HEIGHT)
    OutlineCanvas(canvas)
    CreateShapes(canvas)
    im.FormImage(canvas)

if __name__ == "__main__":
    main()