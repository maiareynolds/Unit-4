#Maia Reynolds
#4/1/18
#sunrise.py - makes sunrise

from ggame import *

def sunmove():
    x=400
    y=700
    sun=CircleAsset(40,LineStyle(1,Color(0xFFFF00,1)),Color(0xFFFF00,1))
    sun1=Sprite(sun,(x,y))
    while y>0:
        y-=1
        sun1.destroy()
        sun1=Sprite(sun,(x,y))

sunmove()
App().run()