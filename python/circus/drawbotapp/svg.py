#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Some functions to convert SVG paths from file to Bézier paths in DrawBot.

from xml.dom import minidom
import random
import os.path
from AppKit import NSPoint
from drawBot.context.baseContext import BezierPath

def svgFileToPaths(fileName):
    paths = []
    svgPaths = getSvgPaths(fileName)
    contours = parseSVG(svgPaths)

    for contour in contours:
        path = contourToPath(contour)
        paths.append(path)

    return paths

def getSvgPaths(fileName):
    u"""Extracts path strings from XML."""
    doc = minidom.parse(fileName)  # parseString also exists
    svgPaths = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
    doc.unlink()
    return svgPaths

def parseSVG(strings):
    u"""Takes a list of path strings and converts them to a list of SVG-command
    tuples."""
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

def reflect(point0, point1):
    u"""Reflects off-curve control point in relation to on-curve one. Used for
    smooth curves."""
    px = point1[0] + (point1[0] - point0[0])
    py = point1[1] + (point1[1] - point0[1])
    return (px, py)

def getRelative(points, pPrevious):
    u"""Calculates absolute coordinates by adding the previous point to the
    relative coordinates."""
    newPoints = []

    for p in points:
        newP = (p[0] + pPrevious[0], p[1] + pPrevious[1])
        newPoints.append(newP)

    return newPoints

def copyPoint(previousPoint, currentPoint):
    u"""Deep copies previous point."""
    previousPoint[0] = currentPoint[0]
    previousPoint[1] = currentPoint[1]

def contourToPath(contour):
    u"""Converts SVG contour to a path in DrawBot."""
    path = BezierPath()
    pPrev = [0.0, 0.0]
    pPrev2 = None
    previousCommand = None

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

            path.moveTo(points[0])
        elif command in ('l', 'h', 'v'):
            if command == 'l':
                if relative:
                    points = getRelative(points, pPrev)
            elif command == 'h':
                if relative:
                    points[0][0] += pPrev[0]

                points[0].append(pPrev[1])
            elif command == 'v':
                points[0].insert(0, pPrev[0])

                if relative:
                    points[0][1] += pPrev[1]

            path.lineTo(points[0])
        elif command == 'c':
            if relative:
                points = getRelative(points, pPrev)

            path.curveTo(*points)
        elif command == 's':
            if relative:
                points = getRelative(points, pPrev)

            # TODO: From the spec:
            #
            # If there is no previous command or if the previous command was
            # not an C, c, S or s, assume the first control point is coincident
            # with the current point
            if previousCommand in ('c', 's'):
                cp = reflect(pPrev2, pPrev)
            else:
                print('TODO: implement, test')
                #copyPoint(cp, points[0])
            path.curveTo(cp, *points)

        elif command == 'z':
            continue

        copyPoint(pPrev, points[-1])

        if command in ('c', 's'):
            pPrev2 = [0.0, 0.0]
            copyPoint(pPrev2, points[-2])
        else:
            pPrev2 = None

        previousCommand = command

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
