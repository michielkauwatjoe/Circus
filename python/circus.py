#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/Circus

import Image
from sizes import Sizes

class Circus(Sizes):
    
    def canvas(self, mode, size):
        u"""
        Build canvas.
        """
        image = Image.new(mode, size, "black")
        image.save("canvas.png")