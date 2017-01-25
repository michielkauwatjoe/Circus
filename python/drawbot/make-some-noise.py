from robofab.ufoLib import UFOReader
from robofab.pens.pointPen import PrintingPointPen
from robofab.glifLib import Glyph
from tnbits.objects.point import Point
import os.path
from wayfinding.pens.cocoapen import CocoaPen
from wayfinding.pens.wayfindingpen import WayFindingPen

class NoisePen(object): 
        
    def beginPath(self):
        self.currentPath = [] 

    def addPoint(self, pt, segmentType=None, smooth=False, name=None, **kwargs):
        self.currentPath.append((pt, segmentType, smooth, name, kwargs))

    def endPath(self):
        u""" Collects segments and flushes."""
        assert self.currentPath is not None
        points = self.currentPath
        self.currentPath = None

        if not points:
            return
        print points

        # Not much more we can do than output a single move segment.
        if len(points) == 1:
            pt, segmentType, smooth, name, kwargs = points[0]
            segments = [("move", [(pt, smooth, name, kwargs)])]
            self._flush(segments)
            return

        segments = []

        # Pop first moveTo point.
        pt, segmentType, smooth, name, kwargs = points[0]
        segments.append(("move", [(pt, smooth, name, kwargs)]))
        points.pop(0)

        currentSegment = []

        for pt, segmentType, smooth, name, kwargs in points:
            currentSegment.append((pt, smooth, name, kwargs))

            # Continue appending next point(s) on offcurve points.
            if segmentType is None:
                continue

            segment = (segmentType, currentSegment)
            segments.append(segment)
            currentSegment = []

        print len(segments)

        self._flush(segments)

    def _flush(self, segments):
        u"""
        The _flush function should be called for each non-empty sub path
        with a list of segments, containing tuples of length 2:
            (segmentType, points)

        The segmentType can be "move", "line", or "curve".  "move" may only
        occur as the first segment, indicating an _open_ path. A _closed_
        path does _not_ start with a "move", in fact it will not contain a
        "move" at all.

        The 'points' field in the 2-tuple is a list of point info tuples. The
        list has 1 or more items, a point tuple has four items:

            (point, smooth, name, kwargs)

        'point' is an (x, y) coordinate pair.

        For a closed path, the initial moveTo point is defined as the last
        point of the last segment.

        The 'points' list of "move" and "line" segments always contains exactly
        one point tuple.
        """
        assert len(segments) >= 1
        path = BezierPath()

        if segments[0][0] == "move":
            # It's an open path.
            print 'open'
            closed = False
            points = segments[0][1]
            assert len(points) == 1
            movePt, smooth, name, kwargs = points[0]
            #p0 = segment[0]
            #del segments[0]
            path.moveTo(movePt)

        nSegments = len(segments)

        for i in range(nSegments):
            segmentType, points = segments[i]
            points = [pt for pt, smooth, name, kwargs in points]

            if segmentType == "line":
                assert len(points) == 1
                pt = points[0]
                if i + 1 != nSegments or not closed:
                    path.lineTo(pt)
            elif segmentType == "curve":
                path.curveTo(*points)
            elif segmentType == "qcurve":
                path._curveToOne(*points)
            elif segmentType == "move":
                pass
                #path.curveTo(*points)
            else: 
                assert 0, "illegal segmentType: %s" % segmentType

        segmentType, points = segments[-1]
        movePt, smooth, name, kwargs = points[-1]
        print movePt

        #if closed:
        path.closePath()
        #else:
        #    path.endPath()
        
        drawPath(path)
    
path = os.path.expanduser('~') + '/Fonts/Input/Input_Fonts/InputSans/InputSansCondensed/InputSansCondensed-Black.ufo'
class TestGlyph: pass
f = UFOReader(path)
msn = " MAKE\nS0ME\nN0ISE"
#msn2 = ['M', 'A', 'K', 'E', 'S', 'zero', 'M', 'E', 'N', 'zero', 'I', 'S', 'E']
lines = [['space', 'M', 'A', 'K', 'E'],
        ['S', 'zero', 'M', 'E'],
        ['N', 'zero', 'I', 'S', 'E']]
points = []
scale(0.25)
gs = f.getGlyphSet()
print gs['S']
pen = NoisePen()

'''
font("InputSansCompressed-Black")
fontSize(256)
text(msn, (100, 100))
'''

stroke(1, 0, 1)
strokeWidth(5)
#fill(1, 1, 0)
#line((100, 100), (200, 200))

translate(0, 2400)
for l in lines:
    save()
    for c in l:
        print c
        g = Glyph(c, gs)
        gs.readGlyph(c, g, pen)
        translate(g.width, 0)
    restore()
    translate(0, -1000)    



#gs.readGlyph("a", g, None)
#g.drawPoints()


#for c in msn2:
    
#    glyph = f[c]
        
#contours = getGlyphContours(points)
#sContours = sortContours(contours)

#for contour in sContours['cw']:
#    pass
    #drawOutlineContour(contour, 'black')
    #translate(800, 0)

#for contour in sContours['ccw']:
#    drawOutlineContour(contour, NSColor.whiteColor())


