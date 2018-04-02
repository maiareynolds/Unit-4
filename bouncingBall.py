#Maia Reynolds
#4/1/18
#bouncingBall.py - moving ball

from ggame import *

cellsize=40
rows=25
cols=13
ball=CircleAsset(cellsize,LineStyle(1,Color(0x1874CD,1)),Color(0x1874CD,1))

ball.x=0
ball.y=0
def move():
    while ball.x<=800 and ball.y<=600:
        ball.x+=1
        ball.y+=1
        Sprite(ball,(ball.x,ball.y))
        if ball.x==0:
            ball.x+=1
        if ball.y==0:
            ball.y+=1
        if ball.y==600:
            ball.y-=600
        if ball.x==800:
            ball.x-=1

move()

App().run()