#!/usr/bin/env python
"""
Ha felsoroljuk az első hat prímszámot: 2, 3, 5, 7, 11 és 13, láthatjuk, hogy mi a 6. prímszám: 13.
Mi az 10001. prímszám?
"""

N = 10001

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

p = 0 # prímszám
n = 0 # amit most ellenörzünk
i = 2

while n != N:
    if isprime(i):
        p = i
        n = n + 1
    i = i + 1

print(p)
