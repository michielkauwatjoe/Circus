#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/Circus

import drawBot

class Circus(object):

    def __init__(self):
        drawBot.newDrawing()
        # A3, TODO: switch to A2.
        drawBot.newPage(1190, 842)
        self.stepIntoArena()
        self.juggle()
        path = '/Users/michiel/Desktop/circus.pdf'
        drawBot.saveImage(path)

    def juggle(self):
        pass

    def stepIntoArena(self):
        u"""
        Step in the arena.
        """
        pass


if __name__ == "__main__":
    circus = Circus()
