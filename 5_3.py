N = int(input("Введите число: "))
counter = 1
for i in range(1, N+1):
    if i % 2 == 0 and counter % 5 != 0:
        print(i, end=" ")
    elif i % 2 == 0 and counter % 5 == 0:
        print(i, end="\n")
    counter += 1
