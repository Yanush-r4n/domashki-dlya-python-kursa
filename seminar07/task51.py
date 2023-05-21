# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли
# объекты имеют одинаковое значение некоторой характеристики, и возвращают
# True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать
# True. Аргумент characteristic - это функция, которая принимает объект и 
# вычисляет его характеристику. В качестве примера характеристики можно взять
# проверку четности из лекции, а можно придумать свою.

def str_characteristic(word: str):
    if len(word) % 2 == 0:
        return True
    
    return False

def int_charackteristic(number: int):
    if number % 2 == 0:
        return True

    return False

# Я делаю проверку именно на схожесть. Если ни один элемент
# списка не подходит под характеристику, соответственно, они схожи.
def same_by(characteristic, objects):
    result = list(filter(characteristic, objects))

    if result == objects or result == list():
        return True
    
    return False


cities = ['Minsk', 'Ivanovo', 'Brest', 'Mogilev']
numbers = [1, 2, 3, 4, 5]

print(same_by(int_charackteristic, numbers))
print(same_by(str_characteristic, cities), end="\n\n")

print(same_by(lambda x: x % 2 == 0, numbers))
print(same_by(lambda x: len(x) % 2 == 0, cities))