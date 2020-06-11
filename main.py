import shapegenerator as sg
import imagemaker as im
import math as mh

#adds from top left start
def AddShapeToCanvas(shape, canvas, xStart, yStart):
    for x in range(xStart, len(shape)+xStart):
        for y in range(yStart, len(shape[0])+yStart):
            if x > WIDTH or y > HEIGHT:
                #print("OUT OF RANGE, SKIPPING")
                continue
            canvas[x][y] = canvas[x][y] or shape[x-xStart][y-yStart]

WIDTH = 500
HEIGHT = 500

#failed polygon    
def CreateNonPolygon(canvas,xStart, yStart, radius=100, sides=150):
    points = sg.PolygonPoints(sides, radius)#[p1, p2, etc]
    #print("points are", points)
    last = -1
    for x,y in points:
        if last == -1:
            last = (x,y)
            continue
        AddShapeToCanvas(sg.MakeLine(last, (x,y)), canvas, xStart+x, yStart+y)
        

def CreateShapes(canvas):
    #CreatePolygon(canvas, 200, 180, 150, 300)
    #for i in range(50):
        #AddShapeToCanvas(sg.MakeSquare((WIDTH//2)+i*5), canvas, WIDTH//2 -i*5, WIDTH//2 -i*5)
    #for i in range(20):
    #AddShapeToCanvas(sg.MakeLine((30,60), (20, 80)), canvas, 10, 200)

def OutlineCanvas(canvas):
    AddShapeToCanvas(sg.MakeRectangle(WIDTH-1, HEIGHT-1), canvas, 0, 0)


def main():
    canvas = sg.MakeCanvas(WIDTH, HEIGHT)
    OutlineCanvas(canvas)
    CreateShapes(canvas)
    im.FormImage(canvas)

if __name__ == "__main__":
    main()