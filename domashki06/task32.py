# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)

sequence = [1, 3, 7, 10, 5, 8]

start = 4
end = 8

diapason = ""

flag = True
for i in range(len(sequence)):
    if sequence[i] >= start and sequence[i] <= end and flag:
        diapason += f"{i}({sequence[i]})"
        flag = False
    elif sequence[i] >= start and sequence[i] <= end:
        diapason += f", {i}({sequence[i]})"

print(diapason)