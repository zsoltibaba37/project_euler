#!/usr/bin/env python
"""
Egy palindrom szám mindkét irányban ugyanúgy olvasható.
Két kétjegyű szám szorzatából előállítható legnagyobb palindrom 9009 = 91 szorozva 99.
Határozd meg két háromjegyű szám szorzatából előállítható legnagyobb palindromot.
"""

def ispalindrom(n):
    return str(n) == str(n)[::-1] # Example 101, 202

n = []
for a in range(100, 999+1):
    for b in range(100,999+1):
        if ispalindrom(a * b):
            n.append(a * b)

print(max(n))
