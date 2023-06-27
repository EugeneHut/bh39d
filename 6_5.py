numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) // 2):
    numbers[i], numbers[~i] = numbers[~i], numbers[i]
print(numbers)

