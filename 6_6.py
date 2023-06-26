my_list = [2, 33, 12, 47, 3, 1, 90, 28, 11]


def sorter(lst):
    even_numbers = []
    odd_numbers = []
    for i in lst:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return even_numbers + odd_numbers


print(sorter(my_list))
