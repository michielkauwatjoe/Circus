from circus.toolbox.bezier.svg2drawbot import *


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

