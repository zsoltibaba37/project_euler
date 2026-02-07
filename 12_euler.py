#!/usr/bin/env python
"""
A háromszögszámok sorozatát a természetes számok összeadásával kapjuk. Tehát a 7. háromszögszám 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 lenne. Az első tíz tag a következő lenne: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,..

1 : 1
3 : 1, 3
6 : 1, 2, 3, 6
10 : 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

Láthatjuk, hogy a 28 az első olyan háromszögszám, amelynek több mint öt osztója van.
Mekkora az első olyan háromszögszám értéke, amelynek több mint ötszáz osztója van?

The solution from:
https://github.com/milcsu09/compiler-x86_64/blob/main/euler/problem12.txt

"""
from numba import njit

@njit
def isqrt_numba(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

@njit
def Div(n):
    d = 0
    r = isqrt_numba(n)
    for i in range(1, r+1):
        if n % i == 0:
            if i * i == n:
                d += 1
            else:
                d += 2
    return d

t = 1
i = 2
while True:
    if Div(t) >= 500:
        print(t)
        break
    t += i
    i += 1




    

