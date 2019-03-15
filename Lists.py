# Jason van Raamsdonk
# Take in the size of the list firstself.
# Then take in the list specific operations followed by parameters
# e.g insert 0 5, remove 6, pop, reverse, sort

    List = []

    N = int(input())

    for i in range(0, N):
        tokens = input().split()

        if tokens[0] == 'insert':
            List.insert(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'print':
            print(List)
        elif tokens[0] == 'remove':
            List.remove(int(tokens[1]))
        elif tokens[0] == 'append':
            List.append(int(tokens[1]))
        elif tokens[0] == 'sort':
            List.sort()
        elif tokens[0] == 'pop':
            List.pop()
        elif tokens[0] == 'reverse':
            List.reverse()
