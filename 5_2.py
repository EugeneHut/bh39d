num1 = float(input("Введите первое число: "))
n = input("Введите действие: ")
num2 = float(input("Введите второе число: "))
if n == "+":
    print("Сумма равна", num1 + num2)
elif n == "-":
    print("Разность равна", num1 - num2)
elif n == "*":
    print("Произведение равно", num1 * num2)
elif n == "/" and num2 == 0:
    print("На ноль делить нельзя")
else:
    print("Деление равно", (num1 / num2))
