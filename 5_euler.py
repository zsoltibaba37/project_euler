#!/usr/bin/env python
"""
A 2520 a legkisebb szám, amely 1-től 10-ig minden számmal maradék nélkül osztható.
Mi a legkisebb pozitív szám, amely egyenletesen osztható az összes számmal 1-től 20-ig?
"""
from math import factorial

def isediv(a):
    for i in range(1,20+1):
        if a % i != 0:
            return False
    return True

for i in range(20,factorial(20),20):
    if isediv(i):
        print(i)
        break
