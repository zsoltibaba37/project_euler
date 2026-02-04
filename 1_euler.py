#!/usr/bin/env python
"""
Ha felsoroljuk a 10 alatti összes olyan természetes számot, amely 3 vagy 5 többszöröse, akkor 3-at, 5-öt, 6-ot és 9-et kapunk. Ezen többszörösök összege 23.
Határozza meg a 3 vagy 5 összes 1000 alatti többszörösének összegét.
"""
n = 0

for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        #print(i)
        n = n + i

print(n)
