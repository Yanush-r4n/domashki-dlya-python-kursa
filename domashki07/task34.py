# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам 

phrase = "пара-ра-рам рам-пам-папам па-ра-па-да"

separated = phrase.split()
counts = list(map(lambda x: x.count('а'), separated))

flag = list(filter(lambda x: x != counts[0], counts))

if flag == list():
    print("Парам пам-пам")
else:
    print("Пам парам")

# Я узнала что существует функция all(), но суть моего решения такая же
# flag = all(count == counts[0] for count in counts)

# if flag:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")