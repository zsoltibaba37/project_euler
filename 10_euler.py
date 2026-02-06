#!/usr/bin/env python
"""
A 10 alatti prímszámok összege 2 + 3 + 5 + 7 = 17.
Határozza meg a kétmillió alatti összes prímszám összegét.
"""
from math import sqrt

def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False # If the number divisible by 'i' then the nuber is not prime 
    return True

N = 2_000_000
f = 0

for i in range(2, N):
    if isprime(i):
        f += i

print(f)
