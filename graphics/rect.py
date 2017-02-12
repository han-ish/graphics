#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
#                                                                           #
#  A simple graphics program.                                               #
#graphics.py is available http://mcsp.wartburg.edu/zelle/python/graphics.py #
# cooked by han-solo http://github.com/han-ish                              #
#                                                                           #
#############################################################################

try:
    from graphics import *
except ImportError:
    raise ImportError("You need to install the graphics library. Check http://mcsp.wartburg.edu/zelle/python/graphics.py")

import math
import time
import random


radius = 500
nodes = 11   # increase the nodes for magic
color = color_rgb(0, 255, 0)
rad = 10

win = GraphWin("Rectangle", 300, 300)
win.setBackground(color_rgb(255, 255, 255))

for i in range(nodes):
    #color = color_rgb(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    x1 = 150 + radius * math.sin(i*3.14*360)/18
    y1 = 150 + radius * math.cos(i*3.14*360)/18
    rad += 1
    for j in range(nodes):
        color = color_rgb(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        x2 = 150 + radius * math.sin(j*3.14*360)/18
        y2 = 150 + radius * math.cos(j*3.14*360)/18
        rect = Rectangle(Point(x2+rad,y2+rad), Point(x2-rad,y2-rad))
        rect.setOutline(color_rgb(random.randrange(0,255), random.randrange(0,255),random.randrange(0,255)))
        rect.draw(win)
        time.sleep(0.1)


win.close()
