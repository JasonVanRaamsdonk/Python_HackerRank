# Essentially an exercise in Lexicographical ordere

# Jason van Raamsdonk


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    init_list = [];

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                new_list = [i, j, k];
                # print(new_list)
                if((i + j + k) != n):
                    init_list.append(new_list)

    print(init_list)
