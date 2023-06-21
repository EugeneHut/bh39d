N = int(input("Введите количество чисел: "))
M = int(input("Кратность: "))
K = int(input("Больше какого: "))
while N > 0:
    K += 1
    if K % M == 0:
        N -= 1
        print(K, end=' ')
