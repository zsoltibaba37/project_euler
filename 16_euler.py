#!/usr/bin/env python

import sys

sys.set_int_max_str_digits(10000)

a = pow(2, 1000)
b = str(a)
n = 0
for i in range(len(b)):
    n += int(b[i])
    
print(n)
