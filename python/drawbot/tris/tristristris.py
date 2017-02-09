# Crude adaptation of Just's dailydrawbot code.

def tri(x, y, w, h, phase, angle):
    #offsetSin = size * sin(radians(angle))
    save()
    translate(w, h)
    rotate(angle)
    polygon((0, 0), (w, 0), (0.5 * w, h + h * phase))
    #rect(0, 0, squareSize, squareSize)
    restore()

canvasW = 900
canvasH = 600
nFrames = 80

w = 90
h = 60
nTris = 10
phase0 = 0.1
phase = 0.1
doPos = True
colors = [(1, 0, 1), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0.8, 0.7, 0.6)]
nc = len(colors)
offset = 0
delta = 0.001

for frame in range(nFrames):
    newPage(canvasW, canvasH)
    frameDuration(1/10)
    fill(0, 1, 0)
    rect(0, 0, canvasW, canvasH)

    # Width loop.
    for j in range(nTris):
        save()

        # Height loop.
        for i in range(nTris):
            ci = (i * j) % nc
            color = colors[ci]
            fill(color[0], color[1], color[2])
            phase += delta
            if phase >= phase0 + 20 * delta:
                pase = phase0
            p = (1 + i * j) % 4  * phase + phase
            tri(0, 0, w, h, p, 180)
            translate(0, h)
        restore()
        translate(w, 0)


saveImage("tristristris.gif")
