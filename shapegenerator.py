import math as mh

def MakeCanvas(x, y):
    x+=1
    y+=1
    arr = []
    for _ in range(x):
        arr.append([])
        for _ in range(y):
            arr[-1].append(False)
    return arr


#draws from top left
def MakeSquare(x):
    return MakeRectangle(x, x)

#draws from top left
def MakeRectangle(x, y):
    arr = MakeCanvas(x, y)
    for i in range(x):#all of start and end arrays
        arr[0][i] = True
        arr[-1][i] = True

    for j in range(y):#first and last of intermediate arrays
        arr[j][0] = True
        arr[j][-1] = True
    return arr

def MakeCircle(radius=50, width=4, detail=0.01):
    arr = MakeCanvas(radius*2, radius*2)
    center = (radius, radius)
    i = -mh.pi
    while i < mh.pi:
        xMod = int(round(mh.cos(i)*radius, 0))
        yMod = int(round(mh.sin(i)*radius, 0))
        arr[radius+xMod][radius+yMod] = True
        i+=detail

    return arr

def MakeLine(start, end, detail=0.01):

    xStart = start[0]
    yStart = start[1]
    xEnd = end[0]
    yEnd = end[1]

    xMax = xStart-xEnd if xStart > xEnd else xEnd-xStart
    yMax = yStart-yEnd if yStart > yEnd else yEnd-yStart
    increm = yMax if yMax > xMax else xMax
    print("increm is", increm)

    arr = MakeCanvas(xMax, yMax)

    xAdd = (xEnd-xStart)/increm
    yAdd = (yEnd - yStart)/increm

    print(xAdd, yAdd)
    print(len(arr), "and", len(arr[0]))
    print(xEnd, yEnd)
    xTrue, yTrue = xStart,yStart

    for _ in range(increm):
        #print(xTrue, yTrue)
        arr[round(xTrue)][round(yTrue)]=True
        xTrue += xAdd
        yTrue += yAdd

    return arr



    


