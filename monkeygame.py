#Maia Reynolds
#3/22/18
#monkeygame.py - best monkey game ever

from ggame import *
from random import randint

Rows=13
Cols=25
cellsize=40

def moveRight(event):
    if monkey.x<(Cols-1)*cellsize:
        monkey.x+=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
def moveLeft(event):
    if monkey.x>0:
        monkey.x-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
def moveUp(event):
    if monkey.y>0:
        monkey.y-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
def moveDown(event):
    if monkey.y<(Rows-1)*cellsize:
        monkey.y+=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
def moveBanana():
    banana.x=randint(0,Cols-1)*cellsize
    banana.y=randint(0,Rows-1)*cellsize


if __name__=="__main__":
    data={}
    data["score"]=0
    green=Color(0x006600,1)
    brown=Color(0x8B4513,1)
    yellow=Color(0xFFFF00,1)
    jungleBox=RectangleAsset(cellsize*Cols,cellsize*Rows,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(cellsize,cellsize,LineStyle(1,brown),brown)
    bananaBox=RectangleAsset(cellsize,cellsize,LineStyle(1,yellow),yellow)
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox,(480,200))
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run()
