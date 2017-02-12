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


radius = 1000 * 2
nodes = 14  # increase the nodes for magic
color = color_rgb(0, 255, 0)
rad = 1 + 1

win = GraphWin("Circle", 300, 300)
win.setBackground(color_rgb(255, 255, 255))

for i in range(nodes):
    x1 = 150 + radius * math.sin(i*3.14*360)/18
    y1 = 150 + radius * math.cos(i*3.14*360)/18
    for j in range(nodes):
        x2 = 150 + radius * math.sin(j*3.14*360)/18
        y2 = 150 + radius * math.cos(j*3.14*360)/18
        circle = Circle(Point(x2, y2), rad)
        #rad += 1
        radius -= 20
        #circle.setOutline(color)
        circle.setFill(color)
        #line = Line(Point(x1,y1), Point(x2,y2))
        #line.setFill(color)
        circle.draw(win)
        #line.draw(win)
        time.sleep(0.1)


win.close()
