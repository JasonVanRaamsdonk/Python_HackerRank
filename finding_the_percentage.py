# Find the average grade from a list of students with a sublist of grades
# only display the average grade from the equested students
# format to 2 decimal points

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks[query_name])

    summation = 0

    for i in student_marks[query_name]:
        summation = summation + i

    average = summation / 3
    # average = float(round(average, 2))

    print("{:0.2f}" .format(average))
