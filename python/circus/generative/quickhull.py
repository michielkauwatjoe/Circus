#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/Circus

from pyhull.convex_hull import ConvexHull
from pyhull.voronoi import VoronoiTess
from pyhull.delaunay import DelaunayTri

class QuickHull(object):
    u"""
    Gets facets from list of points using the Python wrapper for qhull.
    """

    def voronoi(self, points):
        return VoronoiTess(points)

    def delauney(self, points):
        return DelaunayTri(points)

    def convexHull(self, points):
        return ConvexHull(points)

if __name__ == "__main__":
    points = [[-0.5, -0.5], [-0.5, 0.5], [0.5, -0.5], [0.5, 0.5], [0, 0]]
    qhull = Qhull()
    voronoi = qhull.voronoi(points)
    print voronoi.vertices, voronoi.regions
