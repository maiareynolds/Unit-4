#Maia Reynolds
#3/22/18
#monkeygame.py - best monkey game ever


from ggame import *

Rows=20
Cols=35
cellsize=60

def moveRight(event):
    monkey.x+=cellsize
def moveLeft(event):
    monkey.x-=cellsize
def moveUp(event):
    monkey.y-=cellsize
def moveDown(event):
    monkey.y+=cellsize

if __name__=="__main__":
    green=Color(0x006600,1)
    brown=Color(0x8B4513,1)
    jungleBox=RectangleAsset(cellsize*Cols,cellsize*Rows,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(cellsize,cellsize,LineStyle(1,brown),brown)
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run()
