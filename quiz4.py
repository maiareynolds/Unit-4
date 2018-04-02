#Maia Reynolds
#4/2/18
#quiz4.py - ...

def count(x): #counts from 1 up to x
    i=1
    while i<=x:
        print(i)
        i+=1
count(10) #test run

def excitedPrint(string): #takes string, capitalizes, and prints with !!! on end
    final=string.upper()
    print(final+"!!!")
excitedPrint("My name is Maia")#test

def firstLetter(string): #takes string, prints 1st letter
    for ch in string:
        print(ch)
        return
firstLetter("My name is Maia")#test

def repeats(num1,num2,num3):#takes numbers, sees if any are the same
    if num1==num2 or num2==num3 or num3==num1:
        print("True")
    else:
        print("False")
repeats(5,6,5)#test