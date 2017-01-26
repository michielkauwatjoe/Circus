from robofab.ufoLib import UFOReader
from robofab.pens.pointPen import PrintingPointPen
from robofab.glifLib import Glyph
from tnbits.objects.point import Point
import os.path
from wayfinding.pens.cocoapen import CocoaPen
from wayfinding.pens.wayfindingpen import WayFindingPen

from xml.dom import minidom

doc = minidom.parse('make-some-noise.svg')  # parseString also exists
strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()

cmd =['M', 'L', 'l', 'V', 'v', 'C', 'c', 'H', 'h', 'z']
paths = []

for string in strings:
    path = []
    command = None
    pointstring = ''
    points = []

    for c in string:
        
        if c in cmd:
            #print command, len(points)
            if  command is not None:
                path.append((command, points))


            command = c
            if len(pointstring) > 0:
                points.append(pointstring)
            points = []
            pointstring = ''
        else:
            if c == ' ':
                continue
            if c == ',' or c == '-':
                if len(pointstring) > 0:
                    points.append(pointstring)
                if c == '-':
                    pointstring = c
                else:
                    pointstring = ''
            else:
                pointstring += c
            
    paths.append(path)
            
'''
for i, p in enumerate(paths):
    print '\n'
    print strings[i]
    for point in p:
        print point, len(point[1])
'''

M = paths[4]
print strings[4]
print M

path = BezierPath()

p0prev = 0
p1prev = 0

for segment in M:
    print segment
    points = segment[1]
    
    if segment[0] == 'M':
        p0, p1 = points
        p0prev = p0 = float(p0)
        p1prev = p1 = float(p1)
        point = (p0, p1)
        path.moveTo(point)
    elif segment[0] == 'L':
        p0, p1 = points
        p0 = float(p0)
        p1 = float(p1)
        p0prev = p0
        p1prev = p1
        point = (p0, p1)
        path.lineTo(point)
    elif segment[0] == 'l':
        p0, p1 = points
        print p0prev
        p0 = float(p0) + p0prev
        p1 = float(p1) + p1prev
        p0prev = p0
        p1prev = p1
        point = (p0, p1)
        path.lineTo(point)
    elif segment[0] == 'h':
        p0 = points[0]
        p0 = float(p0) + p0prev
        p1 = p1prev
        p0prev = p0
        point = (p0, p1)
        path.lineTo(point)
    elif segment[0] == 'H':
        p0 = points[0]
        p0 = float(p0)
        p1 = p1prev
        p0prev = p0
        point = (p0, p1)
        path.lineTo(point)
    elif segment[0] == 'v':
        p1 = points[0]
        p1 = float(p1) + p1prev
        p0 = p0prev
        p1prev = p1
        point = (p0, p1)
        path.lineTo(point)
    elif segment[0] == 'V':
        p1 = points[0]
        p1 = float(p1)
        p0 = p0prev
        p1prev = p1
        point = (p0, p1)
        path.lineTo(point)

path.closePath()
fill(0, 0, 0)
drawPath(path)