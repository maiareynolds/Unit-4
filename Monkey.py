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
            block=RectangleAsset(50,25,LineStyle(1,green),green)
            s=TextAsset(data["score"],fill=Color(0x00FFFF,1),style="bold 20pt Times")
            Sprite(block,(950,450))
            Sprite(s,(950,450))
def moveLeft(event):
    if monkey.x>0:
        monkey.x-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
            block=RectangleAsset(50,25,LineStyle(1,green),green)
            s=TextAsset(data["score"],fill=Color(0x00FFFF,1),style="bold 20pt Times")
            Sprite(block,(950,450))
            Sprite(s,(950,450))
def moveUp(event):
    if monkey.y>0:
        monkey.y-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
            block=RectangleAsset(50,25,LineStyle(1,green),green)
            s=TextAsset(data["score"],fill=Color(0x00FFFF,1),style="bold 20pt Times")
            Sprite(block,(950,450))
            Sprite(s,(950,450))
def moveDown(event):
    if monkey.y<(Rows-1)*cellsize:
        monkey.y+=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data["score"]+=10
            print(data["score"])
            block=RectangleAsset(50,25,LineStyle(1,green),green)
            s=TextAsset(data["score"],fill=Color(0x00FFFF,1),style="bold 20pt Times")
            Sprite(block,(950,450))
            Sprite(s,(950,450))
def moveBanana():
    banana.x=randint(0,Cols-1)*cellsize
    banana.y=randint(0,Rows-1)*cellsize
def updateScore():
    data["score"]+=10
    data["scoreText"].destroy()
    scoreBox=TextAsset("Score:"+str(data["score"]),fill=Color(0x00FFFF,1),style="bold 20pt Times")
    data["scoreText"]=Sprite(scoreBox,(850,450))

if __name__=="__main__":
    data={}
    data["score"]=0
    green=Color(0x006600,1)
    brown=Color(0x8B4513,1)
    yellow=Color(0xFFFF00,1)
    jungleBox=RectangleAsset(cellsize*Cols,cellsize*Rows,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(cellsize,cellsize,LineStyle(1,Color(0x00FF00,.5)),brown)
    bananaBox=RectangleAsset(cellsize,cellsize,LineStyle(1,yellow),yellow)
    scoretext=TextAsset("Score:",fill=Color(0x00FFFF,1),style="bold 20pt Times")
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox,(480,200))
    Sprite(scoretext,(850,450))
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run()

