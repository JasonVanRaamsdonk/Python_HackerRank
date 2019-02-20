# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#
# a powerful N-dimensional array object sophisticated (broadcasting) functions tools
# for integrating C/C++ and Fortran code useful linear algebra, Fourier transform,
# and random number capabilities
# Besides its obvious scientific uses, NumPy can also be used as an efficient
# multi-dimensional container of generic data. Arbitrary data-types can be defined.
# This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

# The map() function executes a specified function for each item in a iterable.
# The item is sent to the function as a parameter.

# There are four collection data types in the Python programming language:
#
# -> List is a collection which is ordered and changeable. Allows duplicate members.
# -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# -> Set is a collection which is unordered and unindexed. No duplicate members.
# -> Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Jason van Raamsdonk

import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print (A + B)
print (A - B)
print (A * B)
print (A // B)
print (A % B)
print (A ** B)
