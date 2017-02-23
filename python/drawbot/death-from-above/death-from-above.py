from circus.drawbotapp.svg import *
from circus.drawbotapp.transformations import *
from circus.pyobjc.graphics import *
from circus.screensizes import *

def randomSquaresInPaths(paths, n, size, angle, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)

        for path in paths:
            nspath = path._path

            if inside(nspath, x, y):
                s = rotatedSquare(x, y, size, angle)
                drawPath(s)
                break

def randomShapesInPaths(paths, n, size, angle, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)

        for path in paths:
            nspath = path._path

            if inside(nspath, x, y):
                x0 = x - 0.5 * size
                y0 = y - 0.5 * size
                path = BezierPath()
                path.moveTo((x0, y0))
                path.lineTo((x0, y0 + size))
                path.lineTo((x0 - 0.5*size, y0 + size))
                path.lineTo((x0 + 0.5*size, y0 + 1.9*size))
                path.lineTo((x0 + 1.5*size, y0 + size))
                path.lineTo((x0 + size, y0 + size))
                path.lineTo((x0 + size, y0))
                s = rotatedPath(path, x, y, size, angle)
                drawPath(s)
                break

def getLayers():
    layers = []
    layers.append([(1, 0.7, 0), 8000, 20])
    layers.append([(0.1, 1, 0, 0.7), 12000, 14
    ])
    layers.append([(1, 0.2, 0.2, 0.7), 16000, 8])
    layers.append([(0.2, 1, 1, 0.7), 20000, 6])
    layers.append([(0.2, 0.5, 1, 0.7), 24000, 4])
    #layers.append([(0, 0, 0, 0.7), 2400, 10])
    return layers

paths = svgFileToPaths('death-from-above.svg')

# Approximately 40x50 cm (active screenprinting area).

s = list(getDefaultArea('landscape'))
size(*s)
w = width()
h = height()
factor = 2
translate(00, h*1.4)
scale(factor, -factor)
layers = getLayers()

fill(0, 0, 0)
#for p in paths:
#    drawPath(p)


for l in layers:
    fill(*l[0])
    randomSquaresInPaths(paths, l[1], l[2], 45, w, h)
