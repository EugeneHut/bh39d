num = int(input('Введите число: '))
my_list = [i for i in input('Введите список через пробел: ').split()]


def new_list(my_lst, n):
    return my_lst[-n:] + my_lst[:-n]


print(new_list(my_list, num))
