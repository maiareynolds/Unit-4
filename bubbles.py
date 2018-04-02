#Maia Reynolds
#4/1/18
#bubbles.py - creates random bubbles

from random import randint

lred=Color(0xFF4040,1)
mred=Color(0xCD2626,1)
red=Color(0xFF0000,1)
dred=Color(0xB22222,1)
lblue=Color(0x00FFFF,1)
mblue=Color(0x009ACD,1)
dblue=Color(0x483D8B,1)
yellow=Color(0xFFFF00,1)
lgreen=Color(0x00FF00,1)
dgreen=Color(0x228B22,1)
mgreen=Color(0x00C957,1)
llgreen=Color(0x00FF7F,1)
purple=Color(0x8E388E,1)
dpurple=Color(0x800080,1)
lpurple=Color(0x9B30FF,1)
llpurple=Color(0xDA70D6,1)
pink=Color(0xFF1493,1)
drpink=Color(0x8B0A50,1)
lpink=Color(0xFF69B4,1)
mpink=Color(0xEE00EE,1)

def click(event):
    r=randint(10,200)
    x=randint(0,800)
    y=randint(0,700)
    color=randint(1,20)
    if color==1:
        circle=CircleAsset(r,LineStyle(lred,1),lred)
    elif color==2:
        circle=CircleAsset(r,LineStyle(mred,1),mred)
    elif color==3:
        circle=CircleAsset(r,LineStyle(red,1),red)
    elif color==4:
        circle=CircleAsset(r,LineStyle(dred,1),dred)
    elif color==5:
        circle=CircleAsset(r,LineStyle(lblue,1),lblue)
    elif color==6:
        circle=CircleAsset(r,LineStyle(mblue,1),mblue)
    elif color==7:
        circle=CircleAsset(r,LineStyle(dblue,1),dblue)
    elif color==8:
        circle=CircleAsset(r,LineStyle(yellow,1),yellow)
    elif color==9:
        circle=CircleAsset(r,LineStyle(lgreen,1),lgreen)
    elif color==10:
        circle=CircleAsset(r,LineStyle(dgreen,1),dgreen)
    elif color==11:
        circle=CircleAsset(r,LineStyle(mgreen,1),mgreen)
    elif color==12:
        circle=CircleAsset(r,LineStyle(llgreen,1),llgreen)
    elif color==13:
        circle=CircleAsset(r,LineStyle(purple,1),purple)
    elif color==14:
        circle=CircleAsset(r,LineStyle(lred,1),lred)
    Sprite(circle,(x,y))


App().listenMouseEvent("click",click)
App().run()