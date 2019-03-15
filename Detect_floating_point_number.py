# Jason van Raamsdonk
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

N = int(input())

for i in range(0, N):
    values = input()

    print(bool(re.match(r'^[+-]?\d*?\.{1}\d+$' , values)))
