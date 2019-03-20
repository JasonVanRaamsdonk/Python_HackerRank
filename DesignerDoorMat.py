
# -> Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# -> The design should have 'WELCOME' written in the center.
# -> The design pattern should only use |, . and - characters.

N, M = map(int,input().split())

for i in range(int(N/2)):
    for j in range(int((M / 2) - 1) - (i*3)):
        print("-", end='')
    print(".|." * ((i * 2) + 1), end='')

    for j in range(int((M / 2) - 1) - (i*3)):
        print("-", end='')
    print()

print("-" * (int((M - 7)/2)), end='')
print("WELCOME", end='')
print("-" * (int((M - 7)/2)), end='')
print()

for i in reversed(range(int(N/2))):
    for j in range(int((M / 2) - 1) - (i*3)):
        print("-", end='')
    print(".|." * ((i * 2) + 1), end='')

    for j in range(int((M / 2) - 1) - (i*3)):
        print("-", end='')
    print()
