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


for x in range(2,20):
    temp = (x * e) % fi
    print(temp)
    if temp == 1:
        d = x
        break


data = int(input("Enter data to be encrytped: "))
cipher = (data ** e) % n
print("Encrypted data is : ",cipher)
decipher = (cipher ** d) % n
print("Deciphered data is : ",decipher)

