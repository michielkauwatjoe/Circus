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
    
    
path = os.path.expanduser('~') + '/Fonts/Input/Input_Fonts/InputSans/InputSansCondensed/InputSansCondensed-Black.ttf'
#font = fontTools.ttLib.TTFont(path)
f = TTFont(path)
msn = " MAKE\nS0ME\nN0ISE"
msn2 = ['M', 'A', 'K', 'E', 'S', 'zero', 'M', 'E', 'N', 'zero', 'I', 'S', 'E']

glyphNames = f['glyf'].keys()
points = []

for c in msn2:
    g = f['glyf'][c]
    for i, p in enumerate(g.coordinates):
        type = g.flags.tolist()[i]
        start = i - 1 in g.endPtsOfContours
        points.append(Point(p[0], p[1], type=type, start=start))
        
contours = getGlyphContours(points)
print contours

font("InputSansCompressed-Black")
#fontWeight('Black')
fontSize(256)
text(msn, (100, 100))
