size('A2')
fill(0, 10, 10, 100)
h = height()
sq = 100
hsq = 0.5 * sq
qsq = 0.25 * sq

# I
translate(sq, h-2*sq)
save()

polygon((0, qsq), (0, sq), (qsq + hsq, sq))

polygon((0, 0), (sq, 0), (sq, sq))
translate(0, -sq)
rect(0, 0, sq, sq)

# T

translate(1.5*sq, sq)
rect(0, 0, sq, sq)
translate(sq, 0)
rect(0, 0, sq, sq)
translate(0, -sq)
rect(0, qsq, sq, sq)
rect(-hsq, -qsq, 2*sq, qsq)
translate(sq, sq)
rect(0, 0, 0.5*sq, sq)
translate(hsq + qsq, sq)
rect(0, 0, 0.5*sq, 0.5*sq)

# '
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
rect(0, 0, sq + hsq, sq)
rect(0, -qsq, sq, sq)


# New line.
restore()
save()
translate(0, -3*sq)

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

# Underline

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

restore()
save()

#I

#pink
stroke(10, 0, 10, 100)
strokeWidth(1)
#stroke(10, 10, 10, 100)

#T

translate(2*sq, 0)

newPath()
moveTo((0, 0))
lineTo((sq, sq))
lineTo((2*sq, 0))
drawPath()

# Back to first baseline.
restore()
save()

# Whites.
fill(10, 10, 10, 100)

translate(6*sq,0)
polygon((0, 0), (0, hsq), (hsq, 0))
translate(-hsq, 0)
#fill(10, 0, 10, 100)
fill(10, 10, 10, 100)

polygon((0, 0), (qsq, 0), (hsq, -hsq))

restore()
save()
translate(4*sq, -3*sq)
# Whites.
fill(10, 10, 10, 100)
rect(0, 0, qsq, qsq)
translate(2*sq+hsq, hsq)
oval(0, 0, qsq, qsq)