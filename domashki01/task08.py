# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

# 3 2 4 -> yes
# 3 2 1 -> no

raws = int(input("Сколько долек у твоей шоколадки по длине? - "))
columns = int(input("Сколько долек у твоей шоколадки по ширине? - "))
user_num = int(input("Сколько долек ты хочешь отломить? - "))

if user_num in [(raws - 1) * columns, columns, raws * (columns - 1), raws]:
    print(f"Держи {user_num} долек шоколада")
else:
    print(f"Не получится за один раз отломить {user_num} долек шоколада")