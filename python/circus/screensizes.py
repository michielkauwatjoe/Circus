#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Some screenprint size defaults.
# Active area is area that can be printed without tearing the screen. Paper
# size is a best practice approximation, could be anything actually.

screenSizes = {'default': {'paperSize': {'cm': (65, 50)},
    'activeArea': {'cm': (50, 40), 'px': (1134, 1417)}}}

def getDefaultArea(orientation='portrait', unit='px'):
    s = screenSizes['default']['activeArea'][unit]

    if orientation == 'landscape':
        t = (s[1], s[0])
    else:
        t = s

    return t

