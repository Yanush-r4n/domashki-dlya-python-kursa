# Заполните массив элементами арифметической прогрессии. Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

first = 2
difference = 2
quantity = 5

sequence = []

for i in range(1, quantity + 1):
    sequence.append(first + (i - 1) * difference)

print(sequence)