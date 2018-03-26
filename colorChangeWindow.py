#Maia Reynolds
#3/9/18
#colorChangeWindow.py - random color by making function

from ggame import *
from random import randint
red=Color(0xFF0000,1)
blue=Color(0x00FF00,1)
green=Color(0x0000FF,1)
r=RectangleAsset(1200,800,LineStyle(1,red),red)
b=RectangleAsset(1200,800,LineStyle(1,blue),blue)
g=RectangleAsset(1200,800,LineStyle(1,green),green)

def mouseClick(event):
    n=randint(1,3)
    if n==1:
        Sprite(r)
    elif n==2:
        Sprite(b)
    else:
        Sprite(g)

App().listenMouseEvent("click",mouseClick)
App().run()