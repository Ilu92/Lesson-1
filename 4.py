#__author__ = Zdorov Ilya

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = input("Enter number: ")
x = 0
for s in number:
    while int(s) > x:
        x = int(s)
print(x)
