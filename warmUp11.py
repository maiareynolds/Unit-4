#Maia Reynolds
#3/26/18
#warmUp11.py - returns true if = prime and false otherwise

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(prime(7))
print(prime(8))
print(prime(78070))