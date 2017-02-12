from circus.drawbotapp.svg import *
from AppKit import NSAffineTransform

def getAffineTransform(angle, centerX, centerY):
    u"""Rotates at angle around point."""
    at = NSAffineTransform.transform()
    at.translateXBy_yBy_(centerX, centerY)
    at.rotateByDegrees_(angle)
    at.translateXBy_yBy_(-centerX, -centerY)
    return at

def randomPointsInPaths(paths, n, dia, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)
        p = NSPoint(x, y)

        for path in paths:
            if path._path.containsPoint_(p):
                at = getAffineTransform(45, x, y)
                dx = x - 0.5 * dia
                dy =  y - 0.5*dia
                path = BezierPath()
                path.moveTo((dx, dy))
                path.lineTo((dx + dia, dy))
                path.lineTo((dx + dia, dy + dia))
                path.lineTo((dx, dy + dia))
                nsPath = path.getNSBezierPath()
                nsPath = at.transformBezierPath_(nsPath)
                path.setNSBezierPath(nsPath)
                drawPath(path)
                break


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

layers = []
layers.append([(1, 0.7, 0), 8000, 12])
layers.append([(0, 1, 0, 0.7), 12000, 8])
layers.append([(1, 0.2, 0.2, 0.7), 16000, 6])
layers.append([(0.2, 1, 1, 0.7), 20000, 4])
layers.append([(0.2, 0.5, 1, 0.7), 24000, 3])

for l in layers:
    fill(*l[0])
    randomPointsInPaths(paths, l[1], l[2], w, h)