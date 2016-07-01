size('A2')
fill(0, 10, 10, 100)
h = height()
sq = 100
hsq = 0.5 * sq
qsq = 0.25 * sq

# I
translate(sq, h-2*sq)
save()

### LINE 1

scale(0.5)
polygon((0, qsq), (0, sq), (qsq + hsq, sq))

polygon((0, 0), (sq, 0), (sq, sq))
translate(0, -sq)
rect(0, -qsq, sq, sq + qsq)

# T

translate(1.5*sq, sq)

'''
polygon((0, qsq), (0, sq), (qsq + hsq, sq))
polygon((0, 0), (sq, sq), (2*sq, 0), (1.5*sq, 0), (1.5*sq, -hsq - qsq), (hsq, -sq), (hsq, 0))
translate(sq, 0)
#rect(-sq, -sq - qsq, 2*sq, qsq)
polygon((qsq, sq), (sq + hsq, sq), (sq + hsq, 0), (sq + qsq, 0))
translate(sq, 0)
'''

polygon((0, 0), (0, sq), (2*sq, sq), (2*sq, 0), (1.5*sq, 0), (2*sq, -sq), (hsq, -sq), (sq, 0))

# '

translate(2.25*sq, sq)
rect(0, 0, 0.5*sq, 0.5*sq)
translate(qsq, -qsq)
polygon((0, qsq), (qsq, qsq), (qsq, 0), (0, qsq))

# S

translate (qsq, qsq-sq)
oval(0, 0, sq, sq)
rect(hsq, 0, sq, sq)
translate(sq, 0)
rect(0, 0, sq, sq + qsq)
translate(0, -sq)
oval(0, 0, sq, sq)
translate(-sq, 0)
rect(sq, 0, hsq, sq)
translate(0, 0)
polygon((0, 0), (sq, 0), (0, hsq))
#rect(0, -qsq, sq, hq)

# Whites.
fill(10, 10, 10, 100)

translate(sq, sq)
polygon((0, 0), (0, hsq), (hsq, 0))
translate(-hsq, 0)
#polygon((0, 0), (qsq, 0), (hsq, -hsq))

### LINE 2

restore()
save()
translate(0, -2*sq)

# M

rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq)
polygon((0, sq), (sq, sq), (hsq, 0))
translate(sq, 0)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)

# O

translate(sq + hsq, sq - qsq)
rect(0, 0, sq + qsq, sq + qsq)
translate(0, -hsq)
rect(0, 0, sq + qsq, qsq)

# R

translate(sq + hsq + qsq, hsq + qsq)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, 0)
polygon((qsq, 0), (sq, 0), (qsq, sq))
translate(0, sq)
oval(0, 0, sq, sq)

# E

translate(sq + hsq, 0)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq + hsq)
polygon((0, 0), (sq, 0), (0, hsq))
translate(0, -hsq)
rect(0, 0, sq, qsq)
translate(0, -qsq)
polygon((0, 0), (sq, 0), (sq, -sq))

# Strokes

translate(-4.75*sq, qsq)
# Whites.
fill(10, 10, 10, 100)
rect(0, 0, qsq, qsq)
translate(2*sq+hsq, hsq)
oval(0, 0, qsq, qsq)

### LINE 3

restore()
save()
translate(0, -4.5*sq)

# F

rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq + hsq)
polygon((0, -hsq), (sq, -hsq), (sq, hsq))
translate(0, -sq)
rect(0, 0, sq, qsq)

# U

translate(sq + hsq, -hsq)
oval(0, 0, 2*sq,  2*sq)
translate(0, sq)
rect(0, 0, 2*sq, sq)

# N

translate(2.5*sq, -sq)
rect(0, 0, sq, 2*sq)
translate(sq, 2*sq)
polygon((0, 0), (hsq, -hsq), (0, -hsq))
translate(0, -qsq)
polygon((hsq, -hsq), (hsq, -sq), (0, -hsq))
translate(hsq, -2*sq + qsq)
rect(0, 0, sq, 2*sq)

fill(1, 1, 1)
translate(-3.5*sq, sq + hsq + qsq)
oval(0, 0, hsq, hsq)

### LINE 4

restore()
save()
translate(0, -6.5*sq)
scale(0.5)

# T

translate(0, 0)
polygon((qsq, 0), (0, sq), (2*sq, sq), (2*sq, 0), (1.5*sq, 0), (2*sq, -sq), (hsq, -sq), (sq, 0))

# O

translate(2.5*sq, - qsq)
rect(0, 0, sq + qsq, sq + qsq)
translate(0, -hsq)
rect(0, 0, sq + qsq, qsq)

'''
rect(6.5*sq, sq, hsq, sq)
rect(4*sq, sq, 3*sq, qsq)
rect(4*sq, hsq, hsq, hsq)
rect(4*sq, hsq, 6*sq, qsq)
rect(9.5*sq, 0, hsq, hsq)
rect(6.5*sq, 0, 3*sq, qsq)
rect(6.5*sq, -hsq, hsq, hsq)
'''

fill(1, 1, 1)
rect(hsq, sq, qsq, qsq)


### LINE 5

restore()
save()

translate(0, -8.5*sq)

# C

rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq + hsq)
polygon((0, -hsq), (sq, -hsq), (sq, hsq))
translate(0, -sq -hsq)
rect(0, 0, sq, hsq)

# O

translate(sq + hsq, sq - qsq)
rect(0, 0, sq + qsq, sq + qsq)
translate(0, -hsq)
rect(0, 0, sq + qsq, qsq)

# M

translate(sq + hsq + qsq, hsq + qsq)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq)
polygon((0, sq), (sq, sq), (hsq, 0))
translate(sq, 0)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)

rect(1.5*sq, sq, 1.5*sq, qsq)

# Whites.

translate(-3*sq, sq)
fill(1, 1, 1)
rect(0, 0, qsq, qsq)

### LINE 6

restore()
save()

translate(0, -12.5*sq)
rect(0, 0, sq, 2*sq)
translate(sq, sq)
polygon((0, -hsq), (0, sq), (sq, hsq))

# U

translate(sq + hsq, -sq)
oval(0, 0, 2*sq,  2*sq)
translate(0, sq)
rect(0, 0, 2*sq, sq)

# T

translate(2.5*sq, 0)
polygon((0, 0), (0, sq), (2*sq, sq), (2*sq, 0), (1.5*sq, 0), (2*sq, -sq), (hsq, -sq), (sq, 0))

# E

translate(2* sq + hsq, 0)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, 0, sq, sq)
translate(sq, sq + hsq)
polygon((0, 0), (sq, 0), (0, hsq))
translate(0, -hsq)
rect(0, 0, sq, qsq)
translate(0, -qsq)
polygon((0, -hsq), (sq, 0), (sq, -sq))

fill(1, 1, 1)
translate(-5*sq, sq)
oval(0, 0, hsq, hsq)

translate(-2.5*sq, -sq + hsq)
rect(0, 0, qsq, qsq)

### LINE 5

restore()
save()


translate(-sq, -13.5*sq)

for i in range(9):
    translate(sq, 0)
    polygon((0, 0), (hsq, hsq), (sq, 0), (sq, -qsq), (hsq, qsq), (0, -qsq))

translate(sq, 0)
polygon((0, 0), (hsq, hsq), (hsq, qsq), (0, -qsq))
