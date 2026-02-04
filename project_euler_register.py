#!/usr/bin/env python
"""
Egy szám négyzetszám, vagyis négyzetszám, ha egy pozitív egész szám négyzete. Például a 25 négyzetszám, mert 5^2 = 5 * 5 = 25
Az első 5 négyzetszám: 1, 4, 9, 16, 25, és a páratlan négyzetszámok összege 1 + 9 + 25 = 35
Az első 693 ezer négyzetszám közül mennyi az összes páratlan négyzetszám összege?

A number is a perfect square, or a square number, if it is the square of a positive integer. For example, 25 is a square number because 5^2 = 5 * 5 = 25
The first 5 square numbers are: 1, 4, 9, 16, 25 and the sum of the odd squares is 1 + 9 + 25 = 35
Among the first 693 thousand square numbers, what is the sum of all the odd squares?
"""

n = 0
N = 693_000

for i in range(N+1):
    i = i * i
    if i % 2 == 1:
        n = n + i

print(n)

