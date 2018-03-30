#Maia Reynolds
#3/30/18
#triangle.py - area from vertices

from math import sqrt
def distance(x1,y1,x2,y2):
    return (sqrt((x2-x1)**2+(y2-y1)**2))

x1=int(input("What is x1? "))
y1=int(input("What is y1? "))
x2=int(input("What is x2? "))
y2=int(input("What is y2? "))
x3=int(input("What is x3? "))
y3=int(input("What is y3? "))

a=distance(x1,y1,x2,y2)
b=distance(x2,y2,x3,y3)
c=distance(x1,y1,x3,y3)
s=(.5*(a+b+c))
print("Area = "+str(round(sqrt(s*(s-a)*(s-b)*(s-c))),3))