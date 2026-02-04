#!/usr/bin/env python
"""
A Fibonacci-sorozat minden új tagja az előző két tag összeadásával jön létre. Az 1-gyel és 2-vel kezdve az első 10 tag a következő lesz:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
A Fibonacci-sorozat azon tagjainak figyelembevételével, amelyek értéke nem haladja meg a négymilliót, határozd meg a páros értékű tagok összegét.
"""

a = 1
b = 2
s = 0
N = 4_000_000

while a < N:
    if a % 2 == 0:
        s = s + a
    c = a + b
    a = b
    b = c

print(s)

