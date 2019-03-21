import string

def print_rangoli(size):

    alphabet = string.ascii_lowercase
    L = []

    for i in range(size):
        s = "-".join(alphabet[i:n]) # between each element
        L.append(s[::-1] + s[1:]) # cuts "-" from each end e.g -e-d-e- => e-d-e

    width = len(L[0])

    for i in reversed(range(0, size)):
        print(L[i].center(width, "-"))

    for i in range(1, size):
        print(L[i].center(width, "-"))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
