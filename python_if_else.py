#!/bin/python
# Jason van Raamsdonk

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input("Enter a year number: "))

if ( (N % 2 != 0) or ((N % 2 == 0) and (6 <= N <= 20))):
    print("Weird");
else:
    print("Not Weird");
