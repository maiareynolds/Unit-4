#Maia Reynolds
#3/30/18
#multiply.py - teaching multiplication to kids

from random import randint
def ran():
    r=randint(1,5)
    if r==1:
        print("Awesome Job!")
    elif r==2:
        print("You are doing great!")
    elif r==3:
        print("You really know how to multiply!")
    elif r==4:
        print("Way to go!")
    else:
        print("You are great at multiplying!")
def game():
    i=0
    while i<5:
        a=randint(1,12)
        b=randint(1,12)
        c=int(input("What is "+str(a)+"x"+str(b)+"? "))
        if c==(a*b):
            i+=1
            if 1%5==0
            ran()#check
        else:
            print("Sorry, incorrect")


game()