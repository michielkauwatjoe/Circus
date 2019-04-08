# Make. Some. Noise.

from circus.drawbotapp.svg import *

def randomDots(n, dia, w, h):
    for i in range(n):
        x = dia + random.randint(1, w-2*dia)
        y = dia + random.randint(1, h-2*dia)
        x0 = x - 0.5 * dia
        y0 =  y - 0.5 * dia
        oval(x0, y0, dia, dia)

# Approximately 40x50 cm (active screenprinting area).
size(1134, 1417)
w = width()
h = height()
factor = 1
translate(0, h)
scale(factor, -factor)

layers = []
n = 50000
layers.append([(0, 0, 1), n, 2])
layers.append([(1, 0, 0), n, 2])
layers.append([(0, 1, 0), n, 2])

for l in layers:
    fill(*l[0])
    randomDots(l[1], l[2], w, h)
