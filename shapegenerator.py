import math as mh

def FillPixel(canvas, location):
    #print(location)
    if location[0] < 0 or location[0] >= len(canvas):
        return
    if location[1] < 0 or location[1] >= len(canvas[0]):
        return
        #print(len(canvas))
    canvas[location[0]][location[1]] = True

def MakeCanvas(x, y):
    arr = []
    for _ in range(x):
        arr.append([])
        for _ in range(y):
            arr[-1].append(False)
    return arr

#draws from top left
def MakeSquare(canvas, x, start):
    return MakeRectangle(canvas, x, x, start)

#draws from top left
def MakeRectangle(canvas, x, y, start):
    for i in range(x):#fixing y and painting top and bottom
        FillPixel(canvas, (start[0]+i, start[1]))
        #canvas[start[0]+i][start[1]] = 
        FillPixel(canvas, (start[0]+i, start[1]+y))
        #canvas[start[0]+i][start[1]+y] = True

    for j in range(y):#fixing x and painting sides
        FillPixel(canvas, (start[0], start[1]+j))
        #canvas[start[0]][start[1]+j] = True
        FillPixel(canvas, (start[0]+x, start[1]+j))
        #canvas[start[0]+x][start[1]+j] = True

def MakeCircle(canvas, center, radius=50, detail=0.01):
    i = -mh.pi
    while i < mh.pi:
        xMod = int(round(mh.cos(i)*radius, 0))
        yMod = int(round(mh.sin(i)*radius, 0))
        FillPixel(canvas, (xMod+center[0], yMod+center[1]))
        #canvas[xMod+center[0]][yMod+center[0]] = True
        i+=detail

def MakeLine(canvas, start, end, detail=0.01):

    xStart = start[0]
    yStart = start[1]
    xEnd = end[0]
    yEnd = end[1]
    #print("start and end", start, end)
    xMax = xStart-xEnd if xStart > xEnd else xEnd-xStart
    yMax = yStart-yEnd if yStart > yEnd else yEnd-yStart
    increm = yMax if yMax > xMax else xMax
    if increm == 0:#is a single point
        FillPixel(canvas, start)
        return
    #print("increm is", increm)

    xAdd = (xEnd-xStart)/increm
    yAdd = (yEnd - yStart)/increm

    #print("additives are", xAdd, yAdd)
    #print("lens are", len(arr), "and", len(arr[0]))
    xTrue, yTrue = xStart,yStart

    for _ in range(increm):
        #print("currently at", xTrue, yTrue)
        FillPixel(canvas, (round(xTrue), round(yTrue)))
        #canvas[round(xTrue)][round(yTrue)]=True
        xTrue += xAdd
        yTrue += yAdd

def PolygonPoints(numSides, radius, origin=(0,0)):
    arr=[]
    '''for (int i = 0; i < numPoints; i++)
        x = centreX + radius * sin(i * angle);
        y = centreY + radius * cos(i * angle);'''
    tempVal = 2*mh.pi/numSides
    for i in range(numSides):
        x = round(radius*mh.cos(tempVal*i))+origin[0]
        y = round(radius*mh.sin(tempVal*i))+origin[1]
        arr.append((x,y))
    return arr

def MakePolygon(canvas, origin, radius=50, sides=5):
    if sides < 2:
        print("cannot make a polygon with {} side(s)".format(sides))
        return
    points = PolygonPoints(sides, radius, origin)#[p1, p2, etc]
    #print("points are", points)
    last = -1
    for coord in points:
        if last == -1:
            last = coord
            continue
        MakeLine(canvas, coord, last)
        last = coord
    MakeLine(canvas, last, points[0])
    
#see https://en.wikipedia.org/wiki/Hypotrochoid for specifics
def MakeHypotrochoid(canvas, origin, loR, hiR, d, size=10):
    detail = 0.005

    frustration = 0
    frustrationLimit = 50
    takenPositions = set()

    i=1

    tempNum = ((hiR-loR)/loR)
    tempNum2 = (hiR-loR)
    while True:
        x=tempNum2*mh.cos(i)+d*mh.cos(tempNum*i)
        x*=size
        y =tempNum2*mh.sin(i)-d*mh.sin(tempNum*i)
        y*=size
        x,y = int(round(x+origin[0])), int(round(y+origin[1]))

        if (x,y) in takenPositions:
            frustration+=1
            if frustration >= frustrationLimit:
                return
        else:
            takenPositions.add((x,y))
            frustration = 0
        FillPixel(canvas, (x,y))
        i+=detail
    

def MakeMaurer(canvas, origin, seed, otherSeed, size=20):
    max = 60
    detail = 0.003
    i =0
    while i < max:
        k = i * otherSeed * mh.pi / 180
        r = 300 * mh.sin(seed * k)
        x = int(round((r * mh.cos(k))*size + origin[0]))
        y = int(round((r * mh.sin(k))*size + origin[1]))

        FillPixel(canvas, (x+origin[0],y+origin[1]))
        i+=detail



def MakeHyperSpiral(canvas, origin, max, size=80):
    detail = 0.01
    i=0.001

    while i < max:
        x = int(round(mh.cos(i)/i*size + origin[0]))
        y = int(round(mh.sin(i)/i*size + origin[1]))

        FillPixel(canvas, (x,y))
        i+=detail

#looks uninteresting
def MakeCochleoid(canvas, origin, seed, max, size=80):
    detail = 0.05
    i = 0.01
    while i < max:

        x = int(round((seed*mh.cos(i) * mh.sin(i)/ i)*size + origin[0]))
        y = int(round((seed*(mh.sin(i)**2)/i)*size + origin[1]))

        FillPixel(canvas, (x,y))

        i+=detail

#looks uninteresting
def MakeRorshack(canvas, center, a, b, c ,d, max=200, size=150):
    #last = None
    max = 400
    detail = 0.01

    i=0
    while i < max:
        x = mh.cos(a*i) - mh.cos(b*i)**3
        y = mh.sin(c*i) - mh.sin(d*i)**4
        x = int(round(x*size + center[0]))
        y = int(round(y*size + center[1]))
        
        #if last is not None:
        #    MakeLine(canvas, (x,y), last)
        FillPixel(canvas, (x,y))
        #last = (x,y)
        i+=detail

def MakeLissajous(canvas, center, xLobes, yLobes, size=50):
    last = None
    max = 100
    detail=0.01

    i=0
    while i < max:
        x = mh.cos(xLobes*i)
        y = mh.sin(yLobes*i)
        x = int(round(x*size + center[0]))
        y = int(round(y*size + center[1]))

        FillPixel(canvas, (x,y))
        #if last is not None:
            #MakeLine(canvas, (x,y), last)
        #last = (x,y)
        i+=detail


def MakeParametric(canvas, center, size=50):
    #last = None
    max = 100
    i=0.01
    detail=0.01

    while i < max:
        x = None
        y = None
        x = int(round(x*size + center[0]))
        y = int(round(y*size + center[1]))

        FillPixel(canvas, (x,y))
        #if last is not None:
            #MakeLine(canvas, (x,y), last)
        #last = (x,y)
        i+=detail

#only to be copied, does not do anything
def MakeParametric(canvas, center, size=50):
    #last = None
    max = 100
    i=0.01
    detail=0.01

    while i < max:
        x = None
        y = None
        x = int(round(x*size + center[0]))
        y = int(round(y*size + center[1]))

        FillPixel(canvas, (x,y))
        #if last is not None:
            #MakeLine(canvas, (x,y), last)
        #last = (x,y)
        i+=detail

def MakeNormalSpiral(canvas, center, radius=5, maxRadius=80, detail=0.01, radiusSpeed=0.5, reverse=False, start=0):
    # radius, maxRadius=math.inf):
    # i = -math.pi
    # xCord, yCord = pyg.position()
    # xCord += radius
    # while radius < maxRadius:
    #     if(keyboard.is_pressed("esc")):
    #         break
    #     xMod = int(round(math.cos(i)*radius, 0))
    #     yMod = int(round(math.sin(i)*radius, 0))
    #     pyg.moveTo(xCord+xMod, yCord+yMod, duration=moveDuration)
    #     inverseClick()
    #     i+= 0.05
    #     radius += 0.06
    i=start
    while radius < maxRadius:
        xMod = int(round(mh.cos(i)*radius, 0))
        yMod = int(round(mh.sin(i)*radius, 0))
        FillPixel(canvas, (center[0]+xMod, center[1]+yMod))
        if(reverse):
            i-= detail
        else:
            i+=detail
        radius+= radiusSpeed



