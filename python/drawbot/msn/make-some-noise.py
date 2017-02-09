#from circus.toolbox.bezier.svg2drawbot import *

''' lib '''

#from drawBot.context.baseContext import BezierPath
from xml.dom import minidom
import random
import os.path
from AppKit import NSPoint

def reflect(p0, p1, p2, p3):
    u"""Reflects off-curve control point in relation to on-curve one. Used for
    smooth curves."""
    px = p2 + (p2 - p0)
    py = p3 + (p3 - p1)
    return (px, py)

def getRelative(points, p0prev, p1prev):
    newPoints = []

    for p in points:
        newP = (p[0] + p0prev, p[1] + p1prev)
        newPoints.append(newP)

    return newPoints

def contourToPath(contour):
    u"""Converts SVG contour to a path in DrawBot."""
    path = BezierPath()
    p0prev = 0
    p1prev = 0
    cp2 = None

    for segment in contour:
        command = segment[0]
        lower = command.islower()
        upper = command.isupper()
        points = segment[1]

        if command == 'M' or command == 'm':
            p0, p1 = points[0]
            p0prev = p0 = float(p0)
            p1prev = p1 = float(p1)
            point = (p0, p1)
            path.moveTo(point)
        elif command == 'L':
            p0, p1 = points[0]
            p0prev = p0
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'l':
            p0, p1 = points[0]
            p0 = p0 + p0prev
            p1 = p1 + p1prev
            p0prev = p0
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'h':
            p0 = points[0][0]
            p0 = p0 + p0prev
            p1 = p1prev
            p0prev = p0
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'H':
            p0 = points[0][0]
            p0 = p0
            p1 = p1prev
            p0prev = p0
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'v':
            p1 = points[0][0]
            p1 = p1 + p1prev
            p0 = p0prev
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'V':
            p1 = points[0][0]
            p1 = p1
            p0 = p0prev
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif command == 'C':
            p0prev = p4
            p1prev = p5
            cp2 = reflect(p2, p3, p4, p5) # TODO: move to S, s
            path.curveTo(*points)

        elif command == 'c':
            #points = getRelative(points, p0prev, p1prev)
            p0 = points[0][0] + p0prev
            p1 = points[0][1] + p1prev
            p2 = points[1][0] + p0prev
            p3 = points[1][1] + p1prev
            p4 = points[2][0] + p0prev
            p5 = points[2][1] + p1prev
            #p0prev = points[-1][0]
            #p1prev = points[-1][1]
            p0prev = p4
            p1prev = p5
            path.curveTo((p0, p1), (p2, p3), (p4, p5))
            #path.curveTo(*points)
            cp2 = reflect(p2, p3, p4, p5) # TODO: move to S, s
        elif command == 's':
            p0 = points[0][0] + p0prev
            p1 = points[0][1] + p1prev
            p2 = points[1][0] + p0prev
            p3 = points[1][1] + p1prev
            p0prev = p2
            p1prev = p3
            path.curveTo(cp2, (p0, p1), (p2, p3))
        elif command == 'S':
            p0 = points[0][0]
            p1 = points[0][1]
            p2 = points[1][0]
            p3 = points[1][1]
            p0prev = p2
            p1prev = p3
            path.curveTo(cp2, (p0, p1), (p2, p3))

    path.closePath()
    return path
    
def addValueToPoints(valuestring, points):
    u"""Adds the collected character string to the last coordinate in the points
    list."""
    if len(valuestring) == 0:
        return
        
    value = float(valuestring)
        
    if len(points) == 0 or len(points[-1]) == 2:
        points.append([])
        
    points[-1].append(value)
        
def parseSVG(strings):
    u"""Takes a list of path strings and converts them to a list of SVG-command tuples.
    """
    cmd =['m', 'l', 'v', 'c', 'h', 'z', 's']

    paths = []

    for string in strings:
        command = None   # Current command.
        valuestring = ''
        path = []
        points = []

        for c in string:

            if c.lower() in cmd:
                # New command, add previous one to path.
                if  command is not None:
                    path.append((command, points))

                command = c
                addValueToPoints(valuestring, points)

                # Reset.
                points = []
                valuestring = ''
            else:
                # Skip spaces.
                if c == ' ':
                    continue

                # New value.
                if c == ',' or c == '-':
                    addValueToPoints(valuestring, points)

                    # Split on minus.
                    if c == '-':
                        valuestring = c
                    else:
                        valuestring = ''
                else:
                    valuestring += c

        paths.append(path)
    return paths

def getSvgPaths(fileName):
    doc = minidom.parse(fileName)  # parseString also exists
    svgPaths = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
    doc.unlink()
    return svgPaths

''' --- '''

def randomPointsInPaths(paths, n, dia, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)
        p = NSPoint(x, y)
        for path in paths:
            if path._path.containsPoint_(p):
                dx = x - 0.5 * dia
                dy =  y - 0.5*dia
                '''
                #translate(-x, -y)
                rotate(45)
                newPath()
                moveTo((dx, dy))
                lineTo((dx + dia, dy))
                lineTo((dx + dia, dy + dia))
                lineTo((dx, dy + dia))
                closePath()
                drawPath()
                rotate(-45)
                #translate(x, y)
                '''
                oval(x - 0.5 * dia, y - 0.5 * dia, dia, dia)

svgPaths = getSvgPaths('bariol/make-some-noise.svg')
contours = parseSVG(svgPaths)
    

svgPaths = getSvgPaths('bariol/make-some-noise-contra.svg')
contourContra = parseSVG(svgPaths)[0]
pathContra = contourToPath(contourContra)
paths = []


# Approximately 40x50 cm (active screenprinting area).
size(1134, 1417)
w = width()
h = height()
factor = 1
translate(0, h)
scale(factor, -factor)
fill(0, 0, 0)

for contour in contours:
    path = contourToPath(contour)
    paths.append(path)
    #drawPath(path) # Enable for debugging.


# Fills.

'''
fill(0.9, 0.9, 0.7)
randomPointsInPaths([pathContra], 100, 20, w, h)

fill(0.9, 0.7, 0.9)
randomPointsInPaths([pathContra], 800, 10, w, h)
'''

fill(1, 0.7, 0)
randomPointsInPaths(paths, 8000, 12, w, h)


fill(0, 1, 0, 0.7)
randomPointsInPaths(paths, 12000, 8, w, h)

fill(1, 0.2, 0.2, 0.7)
randomPointsInPaths(paths, 16000, 6, w, h)

#fill(0.2, 1, 1, 0.7)
randomPointsInPaths(paths, 20000, 4, w, h)

fill(0.2, 0.5, 1, 0.7)
randomPointsInPaths(paths, 24000, 3, w, h)
