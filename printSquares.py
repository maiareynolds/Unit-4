#Maia Reynolds
#3/28/18
#printSquares.py

def squares(columns,rows):
    print("+"+"--+"*columns)
    r=0
    while r<rows:
        print("|"+"  |"*columns)
        print("+"+"--+"*columns)
        r+=1

squares(2,4)