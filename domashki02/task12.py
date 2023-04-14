
# Пример:
# Ввод: 5 6 -> 2 3

sum = int(input())
product = int(input())

print()

i = 1

while i <= sum // 2:
    if i * (sum - i) == product:
        print (i, sum - i)
    
    i += 1

if not i * (sum - i) == product:
    print("Шото не получается")