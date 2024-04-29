from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MPL import *


def MCL(x0, y0, r): # MCL for region 1
    x = 0
    y = r
    d = 5 - 4*r
    drawSymmetry(x, y, x0, y0)
    while y > x:
        if d < 0: # delE
            d += 4 * (2*x + 3)
            x += 0.5
        else: # delSE
            d += 4 * (2*x - 2*y + 5)
            x += 0.5
            y -= 0.5
        drawSymmetry(x, y, x0, y0)


def drawSymmetry(x, y, x0, y0):
    # drawPixel(x0+x, y0+y)
    # drawPixel(x0-x, y0+y)
    # drawPixel(x0+x, y0-y)
    # drawPixel(x0-x, y0-y)


    # drawPixel(x0+y, y0+x)
    # drawPixel(x0-y, y0+x)
    # drawPixel(x0+y, y0-x)
    # drawPixel(x0-y, y0-x)
    MPL(x0 - x, y0 - y, x0 + x, y0 - y)
    MPL(x0 - y, y0 - x, x0 + y, y0 - x)
    MPL(x0 - y, y0 + x, x0 + y, y0 + x)
    MPL(x0 - x, y0 + y, x0 + x, y0 + y)


def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2d(x, y)
    glEnd()

def drawFilledCircle(x, y, radius):
    glBegin(GL_POINTS)
    for i in range(int(-radius), int(radius) + 1):
        for j in range(int(-radius), int(radius) + 1):
            if i**2 + j**2 <= radius**2:
                glVertex2d(x + i, y + j)
    glEnd()