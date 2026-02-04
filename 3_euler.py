#!/usr/bin/env python
"""
A 13195 prímtényezői az 5, 7, 13 és 29.
Mi a 600851475143 szám legnagyobb prímtényezője?
"""
from math import sqrt

def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False # If the number divisible by 'i' then the nuber is not prime 
    return True

#N = 13195
N = 600851475143
c = []

for i in range(2, N):
    if isprime(i):
        if N % i == 0:
            c.append(i) # If the number divisible with 'i' then add the list
            N = N // i  # Divide 13195 etc..
    if N == 1:
        break

print(max(c))
