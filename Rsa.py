import random
import sympy
import math


p = sympy.randprime(1, 10)
q = sympy.randprime(1, 10)
n = p * q
fi = (p-1) * (q-1)
e = 2
k = random.randint(2, 5)
print(k)


def gcd(a, b):
    temp = 0
    while True:
        temp = a % b
        if temp == 0:
            return b
        a = b
        b = temp


while (e < fi):
    if(gcd(e, fi) == 1):
        break
    else:
        e = e + 1


d = pow(e,-1,fi)


data = int(input("Enter data to be encrytped: "))
cipher = pow(data,e,n)
print("Encrypted data is : ",cipher)
decipher = pow(cipher,d,n)
print("Deciphered data is : ",decipher)
