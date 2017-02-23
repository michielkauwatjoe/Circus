#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Some graphics functions.

from AppKit import NSAffineTransform, NSPoint

def getAffineTransform(angle, centerX, centerY):
    u"""Rotates at angle around point by shifting object to origin first, then
    putting it back after."""
    at = NSAffineTransform.transform()
    at.translateXBy_yBy_(centerX, centerY)
    at.rotateByDegrees_(angle)
    at.translateXBy_yBy_(-centerX, -centerY)
    return at

def inside(nspath, x, y):
    p = NSPoint(x, y)
    if nspath.containsPoint_(p):
        return True

    return False
