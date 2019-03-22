
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the solve function below.
def solve(s):
    L = []
    new_s = s.split(' ') # splits up the input

    for i in (new_s):
        s = str(i)

        L.append(s[:1].upper() + s[1:]) # replaces the first element with its uppercase equivalent

    str_cap = ' '.join(L) # coverts the list to a string

    return str_cap

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
