#!/usr/bin/env python

"""
Egy 2×2-es rács bal felső sarkából kiindulva,
és csak jobbra és lefelé lehet mozogni,
pontosan 6 útvonal vezet a jobb alsó sarokba.

Hány ilyen útvonal van egy 20×20-as rácson keresztül?
"""

from math import factorial

n = factorial(40) // (factorial(20) * factorial(20))

print(n)
