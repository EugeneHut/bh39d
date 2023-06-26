a = int(input("Input: "))


def convert(num):
    b = ''
    while num:
        b += str(num % 2)
        num //= 2
    c = 0
    for i in range(len(b)):
        c += int(b[i]) * (2 ** i)
    return int(b[::-1]), c


print(convert(a))
