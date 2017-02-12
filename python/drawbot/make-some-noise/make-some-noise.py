# Make. Some. Noise.

from circus.drawbotapp.svg import *

def randomDotsInPaths(paths, n, dia, w, h):
    for i in range(n):
        x = random.randint(1, w)
        y = random.randint(1, h)
        p = NSPoint(x, y)

        for path in paths:
            if path._path.containsPoint_(p):
                x0 = x - 0.5 * dia
                y0 =  y - 0.5 * dia
                oval(x0, y0, dia, dia)
                break


paths = svgFileToPaths('bariol/make-some-noise.svg')

# Approximately 40x50 cm (active screenprinting area).
size(1134, 1417)
w = width()
h = height()
factor = 1
translate(0, h)
scale(factor, -factor)

layers = []
layers.append([(1, 0.7, 0), 8000, 12])
layers.append([(0, 1, 0, 0.7), 12000, 8])
layers.append([(1, 0.2, 0.2, 0.7), 16000, 6])
layers.append([(0.2, 1, 1, 0.7), 20000, 4])
layers.append([(0.2, 0.5, 1, 0.7), 24000, 3])

for l in layers:
    fill(*l[0])
    randomDotsInPaths(paths, l[1], l[2], w, h)
