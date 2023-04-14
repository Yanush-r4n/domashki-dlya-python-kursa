# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

user_number = int(input("Введи целое неотрицательное число, а я выведу его факториал: "))

flag = False
while not flag:
    if user_number < 0:
        print("Перечитай условие еще раз")
        user_number = int(input("Введи ЦЕЛОЕ НЕОТРИЦАТЕЛЬНОЕ число, а я выведу его факториал: "))
    else:
        flag = True

factorial = 1
i = 2

while i <= user_number:
    factorial *= i
    i += 1

print(factorial)