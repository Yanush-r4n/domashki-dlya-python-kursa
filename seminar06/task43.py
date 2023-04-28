# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2

def factorial(number: int) -> int:
    '''Возвращает факториал указанного числа (существует факториал чисел от 0 и больше)'''

    result = 1

    if number in [0, 1]:
        return result

    for i in range(2, number + 1):
        result *= i

    return result

list = [1, 2, 1, 3, 4, 3, 1]
dict = dict()
count = 0

for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in dict.values():
    if i == 2:
        count += 1
    elif i > 2:
        count += int(factorial(i) / (2 * factorial((i - 2))))

print(dict)
print(count)