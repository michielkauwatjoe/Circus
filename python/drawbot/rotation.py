from AppKit import NSAffineTransform

def getAffineTransform(angle, point): 
    u"""Rotates at angle around point."""
    x = point[0]
    y = point[1]
    at = NSAffineTransform.transform()
    at.translateXBy_yBy_(x, y)
    at.rotateByDegrees_(angle)
    at.translateXBy_yBy_(-x, -y) 
    return at

def drawCoords(coords, centerX, centerY, rotate=45):
    path = BezierPath()
    at = NSAffineTransform.transform()
    at.translateXBy_yBy_(centerX, centerY)
    at.rotateByDegrees_(rotate)
    at.translateXBy_yBy_(-centerX, -centerY) 
    
    p0 = coords[0]
    path.moveTo((p0[0], p0[1]))
    for coord in coords[1:]:
        path.lineTo((coord[0], coord[1]))
    
    nsPath = path.getNSBezierPath()
    nsPath = at.transformBezierPath_(nsPath)
    path.setNSBezierPath(nsPath)
    drawPath(path)

coords = [(10, 10), (10, 20), (20, 20), (20, 10)]
drawCoords(coords, 15, 15)