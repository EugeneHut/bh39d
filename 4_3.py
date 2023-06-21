n = int(input("Введите число ключей: "))
data1 = {}
data2 = {}
for i in range(n):
    data1['name'] = input("Введите имя: ")
    data1['email'] = input("Введите email: ")
    data2[i] = data1
print(data2)

