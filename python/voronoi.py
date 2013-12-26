#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/Circus

class Voronoi:
    u"""
    Calculate Voronoi cells from list of points.
    """

    def __init__(self, type='taxicab'):
        u"""
        type can be Euclidian or taxi cab.
        """
        self.type = type