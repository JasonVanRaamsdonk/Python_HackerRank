# Jason van Raamsdonk
# printing the two lowest graded students from a list of n elements
# in alphabetical order (name only)

if __name__ == '__main__':

    students = []
    min_vlaue = -1000
    grades = []
    # lowest = []
    final = []

    n = int(input())

    for _ in range(0, n):
        name = input()
        score = float(input())
        new_list = [name, score]
        students.append(new_list)
        if new_list[1] > min_value:
            grades.append(new_list[1])

    #print(grades)
    minimum = min(grades)
    # print(grades)

    for i in range(0, n):
        if minimum in grades:
            grades.remove(minimum)


    grades.sort()
    # print(grades)


    # for i in range(0, len(students) - 2):
    #     grades.remove(max(grades))

    # print(grades)

    for i in range(0, len(students)):
        # print(students[i])
        if grades[0] in students[i]:
            # print(students[i])
            temp = students[i]
            final.append(temp)
        # elif grades[1] in students[i]:
        #     temp = students[i]
        #     # print[temp[0]]
        #     final.append(temp)
        #     # print(students[i])

    final.sort()
    # print(final)

    for i in range(0,2):
        temp = final[i]
        print(temp[0])
