# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам 

vowels = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')

phrase = "паре-ра-рам рам-пум-папам пы-ра-па-да"

separated = phrase.split()
counts = list(map(lambda x: sum(x.count(vowel) for vowel in vowels), separated))

flag = all(count == counts[0] and counts[0] != 0 for count in counts)

if flag:
    print("Парам пам-пам")
else:
    print("Пам парам")