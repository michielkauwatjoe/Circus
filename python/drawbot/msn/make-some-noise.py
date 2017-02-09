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

def contourToPath(contour):
    u"""Converts SVG contour to a path in DrawBot."""
    path = BezierPath()
    p0prev = 0
    p1prev = 0
    cp2 = None

    for segment in contour:
        points = segment[1]

        if segment[0] == 'M':
            p0, p1 = points
            p0prev = p0 = float(p0)
            p1prev = p1 = float(p1)
            point = (p0, p1)
            path.moveTo(point)
        elif segment[0] == 'L':
            p0, p1 = points
            p0 = float(p0)
            p1 = float(p1)
            p0prev = p0
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'l':
            p0, p1 = points
            p0 = float(p0) + p0prev
            p1 = float(p1) + p1prev
            p0prev = p0
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'h':
            p0 = points[0]
            p0 = float(p0) + p0prev
            p1 = p1prev
            p0prev = p0
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'H':
            p0 = points[0]
            p0 = float(p0)
            p1 = p1prev
            p0prev = p0
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'v':
            p1 = points[0]
            p1 = float(p1) + p1prev
            p0 = p0prev
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'V':
            p1 = points[0]
            p1 = float(p1)
            p0 = p0prev
            p1prev = p1
            point = (p0, p1)
            path.lineTo(point)
        elif segment[0] == 'C':
            p0 = float(points.pop(0))
            p1 = float(points.pop(0))
            p2 = float(points.pop(0))
            p3 = float(points.pop(0))
            p4 = float(points.pop(0))
            p5 = float(points.pop(0))
            p0prev = p4
            p1prev = p5
            cp2 = reflect(p2, p3, p4, p5) # TODO: move to S, s
            path.curveTo((p0, p1), (p2, p3), (p4, p5))

        elif segment[0] == 'c':
            p0 = float(points.pop(0)) + p0prev
            p1 = float(points.pop(0)) + p1prev
            p2 = float(points.pop(0)) + p0prev
            p3 = float(points.pop(0)) + p1prev
            p4 = float(points.pop(0)) + p0prev
            p5 = float(points.pop(0)) + p1prev
            p0prev = p4
            p1prev = p5
            path.curveTo((p0, p1), (p2, p3), (p4, p5))
            cp2 = reflect(p2, p3, p4, p5) # TODO: move to S, s
        elif segment[0] == 's':
            p0 = float(points.pop(0)) + p0prev
            p1 = float(points.pop(0)) + p1prev
            p2 = float(points.pop(0)) + p0prev
            p3 = float(points.pop(0)) + p1prev
            p0prev = p2
            p1prev = p3
            path.curveTo(cp2, (p0, p1), (p2, p3))
        elif segment[0] == 'S':
            p0 = float(points.pop(0))
            p1 = float(points.pop(0))
            p2 = float(points.pop(0))
            p3 = float(points.pop(0))
            p0prev = p2
            p1prev = p3
            path.curveTo(cp2, (p0, p1), (p2, p3))
    path.closePath()
    return path

def parseSVG(strings):
    cmd =['M', 'L', 'l', 'V', 'v', 'C', 'c', 'H', 'h', 'z', 's', 'S']
    paths = []

    for string in strings:
        path = []
        command = None
        pointstring = ''
        points = []

        for c in string:

            if c in cmd:
                #print command, len(points)
                if  command is not None:
                    path.append((command, points))


                command = c
                if len(pointstring) > 0:
                    points.append(pointstring)
                points = []
                pointstring = ''
            else:
                if c == ' ':
                    continue
                if c == ',' or c == '-':
                    if len(pointstring) > 0:
                        points.append(pointstring)
                    if c == '-':
                        pointstring = c
                    else:
                        pointstring = ''
                else:
                    pointstring += c

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
                oval(x - 0.5 * dia, y - 0.5 * dia, dia, dia)

svgPaths = getSvgPaths('make-some-noise-bariol.svg')
contours = parseSVG(svgPaths)
svgPaths = getSvgPaths('make-some-noise-bariol-contra.svg')
contourContra = parseSVG(svgPaths)[0]
pathContra = contourToPath(contourContra)
paths = []
size('A2')
factor = 1.6
translate(-80, 1700)
scale(factor, -factor)
fill(0.5, 0.5, 0.5)

for contour in contours:
    path = contourToPath(contour)
    paths.append(path)
    #drawPath(path) # Enable for debugging.

w = width()
h = height()

fill(0.9, 0.9, 0.7)
randomPointsInPaths([pathContra], 100, 20, w, h)

fill(0.9, 0.7, 0.9)
randomPointsInPaths([pathContra], 800, 10, w, h)

fill(1, 0.7, 0)
randomPointsInPaths(paths, 8000, 12, w, h)

fill(0, 1, 0, 0.7)
randomPointsInPaths(paths, 12000, 8, w, h)

fill(1, 0.2, 0.2, 0.7)
randomPointsInPaths(paths, 16000, 6, w, h)

fill(0.2, 1, 1, 0.7)
randomPointsInPaths(paths, 20000, 4, w, h)

fill(0.2, 0.5, 1, 0.7)
randomPointsInPaths(paths, 24000, 3, w, h)

