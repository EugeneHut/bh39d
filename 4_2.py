text = input('Введите текст: ')
my_dict = {i: text.count(i) for i in text}
print(my_dict)
