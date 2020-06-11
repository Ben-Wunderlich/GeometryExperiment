import math as mh

def MakeCanvas(x, y):
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

def MakeCircle(radius=50, width=4):
    arr = MakeCanvas(radius*2, radius*2)
    #center = (radius, radius)

    r2 = radius**2
    lowR2 = r2 - width/2
    hiR2 = r2 + width/2
    for x, line in enumerate(arr):
        for y, el in enumerate(line):
            sqSum = (x+radius)**2 + (y+radius)**2
            if lowR2 <= sqSum <= hiR2:
                arr[x][y] = True
    return arr