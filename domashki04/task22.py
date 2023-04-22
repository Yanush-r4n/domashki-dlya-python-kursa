import os
os.system('cls')

first_size = int(input("Укажи длину первой последовательности чисел: "))
second_size = int(input("Укажи длину второй последовательности чисел: "))

first_set = set()
second_set = set()

print("Заполни первую последовательность")
for i in range(first_size):
    first_set.add(int(input()))

print("Заполни вторую последовательность")
for i in range(second_size):
    second_set.add(int(input()))

# first_set = {1, 5, 7, 6, 4, 1, 6, 2, 7}
# second_set = {8, 6, 9, 5, 4, 3, 9, 7, 2, 1}

resutl = list(first_set.intersection(second_set))
resutl.sort()
print(resutl)