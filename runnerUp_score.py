# Jason van Raamsdonk
# program to print the second highest element of an inputted my_array
# first input is the array size, second to n inputs are the array elements

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    current = min(arr)


    for i in range(0, n):
        if arr[i] > current and arr[i] < max(arr):
            current = arr[i]



    print(current)
    # print(max(arr))
