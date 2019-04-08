# Make. Some. Noise.
import math
from circus.drawbotapp.svg import *

def circle(x, y, dia):
    x = x - 0.5 * dia
    y =  y - 0.5 * dia
    oval(x, y, dia, dia)

def ring(x, y, distance, dia, n):
    offset = random.randint(0, 360)
    for i in range(n):
        angle = i * 360 / n + offset
        r = angle * math.pi / 180
        
        xOffset = -dia/ 2 + random.random() * dia
        yOffset = -dia / 2 + random.random()
        x1 = x + distance * math.cos(r) + xOffset
        y1 = y + distance * math.sin(r) + yOffset
        circle(x1, y1, dia)

def splat(x, y, dia):
    #circle(x, y, dia*0.6)
    r0 = random.randint(3, 6)

    r1 = random.randint(9, 12)
    r2 = random.randint(20, 24)
    r3 = random.randint(20, 24)
    ring(x, y, 0.3 * dia, dia / 3, r0)
    ring(x, y, 0.6 * dia, dia /4, r1)
    ring(x, y, 0.8 * dia, dia / 6, r2)
    ring(x, y, 1 * dia, dia / 20, r3)

def randomDotsInPaths(paths, n, dia, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)
        p = NSPoint(x, y)

        for path in paths:
            if path._path.containsPoint_(p):
                splat(x, y, dia)
                break

def draw():
    layers = []
    n = 15000
    layers.append([(1, 0.7, 0, 0.3), n, 2])
    #layers.append([(0, 1, 0, 0.7), n, 2])
    layers.append([(1, 0.2, 0.2, 0.7), n, 2])
    layers.append([(0.2, 1, 1, 0.7), n, 2])
    #layers.append([(0.2, 0.5, 1, 0.7), n, 2])

    for l in layers:
        fill(*l[0])
        randomDotsInPaths(paths, l[1], l[2], w, h)

paths = svgFileToPaths('gGflat.svg')

# Approximately 40x50 cm (active screenprinting area).
size(500, 500)
w = width()
h = height()
factor = 1
translate(0, h)
scale(factor, -factor)

#splat(250, 250, 10)
jk/moved
draw()

