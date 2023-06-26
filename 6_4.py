my_list = [22, 'hello', True, 22, 'World', 'people', False, 22.33]


# def list_filter_str(lst):
#     lst = [i for i in lst if isinstance(i, str)]
#     return list(lst)


def list_filter_str2(lst):
    i = 0
    while i < len(lst):
        if not isinstance(lst[i], str):
            del lst[i]
        else:
            i += 1
    return lst


print(list_filter_str2(my_list))
