#!/usr/bin/env python
"""
Egy Pitagorasz-hármas három természetes szám halmaza, a < b < c, ahol a^2 + b^2 = c^2.
Például 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
Pontosan egy ilyan Pitagorasz-hármas létezik, amelyre a + b + c = 1000. Határozza meg az abc szorzatot.
"""
for a in range(1, 1000):
    for b in range(a,1000):
        c = 1000 - a - b
        if (a*a) + (b*b) == c*c:
            #print(f"{a},{b},{c}")
            print(a*b*c)

