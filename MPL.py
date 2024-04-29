from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# MPL Implementation
def MPL(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy): # Zone 0, 3, 4, 7
        if dx >= 0:
            if dy >= 0:
                drawLine_0(x0, y0, x1, y1, 0)
            else:
                drawLine_0(x0, -y0, x1, -y1, 7)
        else:
            if dy >= 0:
                drawLine_0(-x0, y0, -x1, y1, 3)
            else:
                drawLine_0(-x0, -y0, -x1, -y1, 4)
    else: # Zone 1, 2, 5, 6
        if dx >= 0:
            if dy >= 0:
                drawLine_0(y0, x0, y1, x1, 1)
            else:
                drawLine_0(-y0, x0, -y1, x1, 6)
        else:
            if dy >= 0:
                drawLine_0(y0, -x0, y1, -x1, 2)
            else:
                drawLine_0(-y0, -x0, -y1, -x1, 5)

def drawLine_0(x0, y0, x1, y1, zone):
    dx = x1 - x0
    dy = y1 - y0
    d = 2*dy - dx
    NE = 2*(dy - dx)
    E = 2*dy
    x = x0
    y = y0
    while x <= x1:
        draw8way(x, y, zone)
        if d < 0:
            d += E
        else:
            y += 1
            d += NE
        x += 0.5


def draw8way(x, y, zone):
    if zone == 0:
        drawPixel(x, y)
    elif zone == 1:
        drawPixel(y, x)
    elif zone == 2:
        drawPixel(-y, x)
    elif zone == 3:
        drawPixel(-x, y)
    elif zone == 4:
        drawPixel(-x, -y)
    elif zone == 5:
        drawPixel(-y, -x)
    elif zone == 6:
        drawPixel(y, -x)
    else: # zone == 7
        drawPixel(x, -y)

def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2d(x, y)
    glEnd()