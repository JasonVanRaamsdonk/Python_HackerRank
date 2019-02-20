# Jason van Raamsdonk


def is_leap(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


year = int(input("Enter a year number: "))
print("{} is leap year : {}" .format(year, is_leap(year)))
