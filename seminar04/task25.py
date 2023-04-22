# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. Порядок символов исходной строки не меняется.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

import timeit

version_1 = '''
user_string = "a a a b c a a d c d d"
string = user_string.replace(" ", "")

current_index = 0

for symbol in string:
    count = 0

    for i in range(current_index, -1, -1):
        if i == current_index:
            pass
        elif symbol == string[i]:
            count += 1

    current_index += 1

    if count == 0:
        print(f"{symbol}")
    else:
        print(f"{symbol}_{count}")
'''


version_2 = '''
user_string = "a a a b c a a d c d d"
string = user_string.replace(" ", "")

count = {}
result = []

for key in string:
    if key in count:
        count[key] += 1
    else:
        count[key] = 0

    if count[key] == 0:
        result.append(key)
    else:
        result.append(key + "_" + str(count[key]))

result = " ".join(result)

print(result)
'''


version_3 = '''
user_string = "a a a b c a a d c d d"
string = user_string.replace(" ", "")

count = {}
result = []

for char in set(string):
    count[char] = 0

for char in string:
    if count[char] == 0:
        result.append(char)
    else:
        result.append(char + "_" + str(count[char]))

    count[char] += 1

result = " ".join(result)

print(result)
'''


t1 = timeit.Timer(stmt=version_1).timeit(number=100000)
t2 = timeit.Timer(stmt=version_2).timeit(number=100000)
t3 = timeit.Timer(stmt=version_3).timeit(number=100000)

print(f"first: {t1}")
print(f"second: {t2}")
print(f"third: {t3}")