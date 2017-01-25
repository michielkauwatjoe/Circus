from fontTools.ttLib import TTFont
from tnbits.objects.point import Point
import os.path

def getGlyphContours(points):
    u"""
    Splits up points into separate closed outlines based on start value of point.
    """ 
    contours = []

    for i, point in enumerate(points):

        if i == 0:
            contour = [point]
        elif point.start is True:
            contour.append(contour[0])
            contours.append(contour)
            contour = [point]
        else:
            contour.append(point)

        if i == len(points) - 1:
            contour.append(contour[0])
            contours.append(contour)
    return contours

def shoelace(part):
    u"""
    Shoelace algorithm to determine clock direction.
    """
    oncurves = []
    for point in part:
        if point.type == 1:
            oncurves.append(point)

    total = 0

    for i, point in enumerate(oncurves):
        if i == len(oncurves) - 1:
            j = 0
        else:
            j = i + 1

        total += (oncurves[j].x - point.x) * (oncurves[j].y + point.y)

    return total

def sortContours(contours):
    u"""
    Sorts glyph contours based on clock direction.
    """ 
    sContours = {'cw': [], 'ccw': []} 

    for contour in contours:
        if shoelace(contour) < 0:
            sContours['ccw'].append(contour)
        else:
            sContours['cw'].append(contour)

    return sContours
    
def drawOutlineContour(contour, color):
    u"""
    Draws vector points using a CocoaPen.
    """
    if len(contour) == 0:
        return

    path = BezierPath()
    print 'new path'
    curves = []
    curve = [contour[0]]

    for i, point in enumerate(contour[1:]):

        if point.type == 0:
            offcurve = True
        else:
            offcurve = False

        if offcurve is True:
            curve.append(point)
        else:
            curve.append(point)
            curves.append(curve)
            curve = [point]

    point0 = curves[0][0]
    p0 = (point0.x, point0.y)
    path.moveTo(p0)

    for curve in curves:
        drawCurve(curve, path)

    path.closePath()
    fill(0, 0, 0)
    drawPath(path)

def drawCurve(curve, path):
    assert len(curve) > 1

    if len(curve) == 2:
        point = curve[-1]
        coordinates = (point.x, point.y)
        path.lineTo(coordinates)
    elif len(curve) == 3:
        onCurve0 = curve[0]
        offCurve = curve[1]
        onCurve1 = curve[2]

        x0 = onCurve0.x + (offCurve.x - onCurve0.x) * 1 / 1.3
        y0 = onCurve0.y + (offCurve.y - onCurve0.y) * 1 / 1.3

        offCurve0 = (x0, y0)

        x1 = onCurve1.x - (onCurve1.x - offCurve.x) * 1 / 1.3
        y1 = onCurve1.y - (onCurve1.y - offCurve.y) * 1 / 1.3
        offCurve1 = (x1, y1)

        #self.drawMarkerCircle(offCurve0, NSColor.yellowColor(), 4)
        #self.drawMarkerCircle(offCurve1, NSColor.yellowColor(), 4)
        #NSColor.blackColor().set()
        fill(0, 0, 0)
        onCurve = (onCurve1.x, onCurve1.y)
        path.curveTo(offCurve0, offCurve1, onCurve)
    else:

        offCurve0 = curve[1]
        offCurve1 = curve[2]
        curve0 = curve[:2]
        curve1 = curve[2:]

        # Implied point.
        x = offCurve0.x + (offCurve1.x - offCurve0.x) * 0.5
        y = offCurve0.y + (offCurve1.y - offCurve0.y) * 0.5
        newOnCurve = Point(x, y, 1)
        #drawMarkerCircle((x, y), NSColor.greenColor(), 4)

        curve0.append(newOnCurve)
        curve1.insert(0, newOnCurve)
        (curve0, path) # First part, length is three.
        drawCurve(curve1, path) # Second part, length >= 3.
    
path = os.path.expanduser('~') + '/Fonts/Input/Input_Fonts/InputSans/InputSansCondensed/InputSansCondensed-Black.ttf'
#font = fontTools.ttLib.TTFont(path)
f = TTFont(path)
msn = " MAKE\nS0ME\nN0ISE"
#msn2 = ['M', 'A', 'K', 'E', 'S', 'zero', 'M', 'E', 'N', 'zero', 'I', 'S', 'E']
msn2 = ['S']
glyphNames = f['glyf'].keys()
points = []
#scale(0.3)

for c in msn2:
    g = f['glyf'][c]
    for i, p in enumerate(g.coordinates):
        type = g.flags.tolist()[i]
        start = i - 1 in g.endPtsOfContours
        points.append(Point(p[0], p[1], type=type, start=start))
        
contours = getGlyphContours(points)
sContours = sortContours(contours)

for contour in sContours['cw']:
    drawOutlineContour(contour, 'black')
    translate(800, 0)

#for contour in sContours['ccw']:
#    drawOutlineContour(contour, NSColor.whiteColor())

'''
font("InputSansCompressed-Black")
fontSize(256)
text(msn, (100, 100))
'''