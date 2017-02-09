from drawBot.context.baseContext import BezierPath
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
