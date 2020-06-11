import shapegenerator as sg
import imagemaker as im

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

def CreateShapes(canvas):
    #for i in range(10):
    #    AddShapeToCanvas(sg.MakeSquare(300), canvas, i*5, i*5)
    AddShapeToCanvas(sg.MakeLine((0,0), (20, 50)), canvas, 40, 40)

def OutlineCanvas(canvas):
    AddShapeToCanvas(sg.MakeRectangle(WIDTH-1, HEIGHT-1), canvas, 0, 0)


def main():
    canvas = sg.MakeCanvas(WIDTH, HEIGHT)
    OutlineCanvas(canvas)
    CreateShapes(canvas)
    im.FormImage(canvas)

if __name__ == "__main__":
    main()