#!/usr/bin/env python
"""
Tehát az első tíz természetes szám négyzetösszege és az összeg négyzete közötti különbség 3025-385=2640
Határozza meg az első száz természetes szám négyzetösszege és az összeg négyzete közötti különbséget.
"""
N = 100

sS = 0
aS = 0

def sumSquer(n):
    a = 0
    for i in range(1,n+1):
        a = a + i ** 2
    return a

def addSquer(n):
    a = 0
    for i in range(1,n+1):
        a = a + i
    return a ** 2

sS = sumSquer(N)
aS = addSquer(N)

#print(sS)
#print(aS)

print(aS-sS)
