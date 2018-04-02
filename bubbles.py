#Maia Reynolds
#4/1/18
#bubbles.py - creates random bubbles

from random import randint
red=Color(0xCD2626,1)
lblue=Color(0x00FFFF,1)
mblue=Color(0x009ACD,
def click(event):
    r=randint(10,200)
    x=randint(0,800)
    y=randint(0,700)
    


App().listenMouseEvent("click",click)
App().run()