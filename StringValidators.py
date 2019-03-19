
if __name__ == '__main__':
    s = input()

    alphanumeric = any([c.isalnum() for c in s])

    alphabetic = any([c.isalpha() for c in s])

    digit = any([c.isdigit() for c in s])

    lowercase = any([c.islower() for c in s])

    uppercase  =any([c.isupper() for c in s])

    print("{}\n{}\n{}\n{}\n{}".format(alphanumeric, alphabetic, digit, lowercase, uppercase))
