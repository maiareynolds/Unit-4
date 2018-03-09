#Maia Reynolds
#3/9/18
#colorChangeWindow.py - random color by making function

from ggame import *
red=Color(0xFF0000,1)
r=RectangleAsset(800,800,LineStyle(1,red),red)
Sprite(r)
def colorChange():
    r=RectangleAsset(800,800,LineStyle(1,red),red)
    Sprite(r)

App().listenMouseEvent("click",mouseClick)
App.run()

colorChange()