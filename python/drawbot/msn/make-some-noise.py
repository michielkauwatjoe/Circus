#from circus.toolbox.bezier.svg2drawbot import *

''' lib '''

#from drawBot.context.baseContext import BezierPath
from xml.dom import minidom
import random
import os.path
from AppKit import NSPoint

def reflect(point0, point1):
    u"""Reflects off-curve control point in relation to on-curve one. Used for
    smooth curves."""
    px = point1[0] + (point1[0] - point0[0])
    py = point1[1] + (point1[1] - point0[1])
    return (px, py)

def getRelative(points, pPrevious):
    newPoints = []

    for p in points:
        newP = (p[0] + pPrevious[0], p[1] + pPrevious[1])
        newPoints.append(newP)

    return newPoints

def setPreviousPoint(previousPoint, currentPoint):
    previousPoint[0] = currentPoint[0]
    previousPoint[1] = currentPoint[1]

def contourToPath(contour):
    u"""Converts SVG contour to a path in DrawBot."""
    path = BezierPath()
    pPrev = [0.0, 0.0]
    cp = None

    for segment in contour:
        command = segment[0]
        points = segment[1]

        relative = False

        if command.islower():
            relative = True
            
        command = command.lower()

        if command == 'm':
            if relative:
                points = getRelative(points, pPrev)
                
            setPreviousPoint(pPrev, points[0])
            path.moveTo(points[0]
)
        elif command == 'l':
            if relative:
                points = getRelative(points, pPrev)
                
            setPreviousPoint(pPrev, points[0])
            path.lineTo(points[0])

        elif command == 'h':            
            if relative:
                points[0][0] += pPrev[0]

            points[0].append(pPrev[1])
            setPreviousPoint(pPrev, points[0])
            path.lineTo(points[0])
            
        elif command == 'v':
            points[0].insert(0, pPrev[0])

            if relative:
                points[0][1] += pPrev[1]

            setPreviousPoint(pPrev, points[0])
            path.lineTo(points[0])
    
        elif command == 'c':
            if relative:
                points = getRelative(points, pPrev)
                
            path.curveTo(*points)
            # TODO: move to S, s?
            cp = reflect(points[-2], points[-1])
            setPreviousPoint(pPrev, points[-1])

        elif command == 's':
            if relative:
                points = getRelative(points, pPrev)
                
            setPreviousPoint(pPrev, points[-1])
            path.curveTo(cp, *points)

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
    drawPath(path) # Enable for debugging.


# Fills.

'''
fill(0.9, 0.9, 0.7)
randomPointsInPaths([pathContra], 100, 20, w, h)

fill(0.9, 0.7, 0.9)
randomPointsInPaths([pathContra], 800, 10, w, h)
'''

fill(1, 0.7, 0)
randomPointsInPaths(paths, 8000, 12, w, h)


#fill(0, 1, 0, 0.7)
#randomPointsInPaths(paths, 12000, 8, w, h)

#fill(1, 0.2, 0.2, 0.7)
#randomPointsInPaths(paths, 16000, 6, w, h)

#fill(0.2, 1, 1, 0.7)
#randomPointsInPaths(paths, 20000, 4, w, h)

#fill(0.2, 0.5, 1, 0.7)
#randomPointsInPaths(paths, 24000, 3, w, h)
