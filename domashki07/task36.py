random_bunch = "house=дом car=машина men=человек tree=дерево"

result = random_bunch.split()
result = list(map(lambda x: x.replace('=', ' ').split(), result))
result = tuple(map(tuple, result))

print(result)