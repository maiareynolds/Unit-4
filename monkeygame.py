#Maia Reynolds
#3/22/18
#monkeygame.py - best monkey game ever

from ggame import *
from random import randint

Rows=13
Cols=25
cellsize=40

def moveRight(event): #moves right one cell if possible
    if monkey.x<(Cols-1)*cellsize:
        monkey.x+=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
def moveLeft(event): #moves left one cell if possible
    if monkey.x>0:
        monkey.x-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
def moveUp(event): #moves up one cell if possible
    if monkey.y>0:
        monkey.y-=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
def moveDown(event): #moves down one cell if possible
    if monkey.y<(Rows-1)*cellsize:
        monkey.y+=cellsize
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
def moveBanana(): #moves banana randomly within the screen
    data["frames"]=0 #resetting the timer for the function
    banana.x=randint(0,Cols-1)*cellsize
    banana.y=randint(0,Rows-1)*cellsize
def updateScore(): #adds 10 points to score and displays new text at bottom of screen
    data["score"]+=10
    data["scoreText"].destroy() #removes old writing
    scoreBox=TextAsset("Score = "+str(data["score"]))
    data["scoreText"]=Sprite(scoreBox,(0,Rows*cellsize-30))
def step(): #keeps track of frames that have happened, moves banana if more than 300 frames since last move
    data["frames"]+=1
    if data["frames"]==300:
        moveBanana()

if __name__=="__main__": #sets up and runs game
    data={}
    data["score"]=0
    data["frames"]=0
    green=Color(0x006600,1)#graphics
    brown=Color(0x8B4513,1)
    yellow=Color(0xFFFF00,1)
    jungleBox=RectangleAsset(cellsize*Cols,cellsize*Rows,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(cellsize,cellsize,LineStyle(1,brown),brown)
    bananaBox=RectangleAsset(cellsize,cellsize,LineStyle(1,yellow),yellow)
    scoreBox=TextAsset("Score = 0")
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox,(480,200))
    data["scoreText"]=Sprite(scoreBox,(0,Rows*cellsize-30))
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run(step)
