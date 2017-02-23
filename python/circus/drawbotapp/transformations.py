#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Some graphics transformations.

from drawBot.context.baseContext import BezierPath
from circus.pyobjc.graphics import getAffineTransform

def rotatedSquare(x, y, size, angle):
    u"""Draws a square of size and rotates it around center by angle."""
    x0 = x - 0.5 * size
    y0 =  y - 0.5 * size
    at = getAffineTransform(angle, x, y)
    path = BezierPath()
    path.moveTo((x0, y0))
    path.lineTo((x0 + size, y0))
    path.lineTo((x0 + size, y0 + size))
    path.lineTo((x0, y0 + size))
    nsPath = path.getNSBezierPath()
    nsPath = at.transformBezierPath_(nsPath)
    path.setNSBezierPath(nsPath)
    return path

def rotatedPath(path, x, y, size, angle):
    u"""Draws a path of size and rotates it around center by angle."""
    x0 = x - 0.5 * size
    y0 =  y - 0.5 * size
    at = getAffineTransform(angle, x, y)
    nsPath = path.getNSBezierPath()
    nsPath = at.transformBezierPath_(nsPath)
    path.setNSBezierPath(nsPath)
    return path

