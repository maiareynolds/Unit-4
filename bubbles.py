#Maia Reynolds
#4/1/18
#bubbles.py - creates random bubbles

from random import randint
lred=Color(0xFF4040,1)
mred=Color(0xCD2626,1)
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
def click(event):
    r=randint(10,200)
    x=randint(0,800)
    y=randint(0,700)
    


App().listenMouseEvent("click",click)
App().run()