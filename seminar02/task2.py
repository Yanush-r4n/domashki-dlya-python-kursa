# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

from random import randint

user_number = int(input("Какое количество арбузов на прилавке лежит? - "))

flag = False
while not flag:
    if user_number < 0:
        print("Они типа ещё не выросли?")
        user_number = int(input("Так сколько? -  "))
    elif user_number == 0:
        print("Ну не, на прилавке не пусто")
        user_number = int(input("Так сколько же? - "))
    else:
        flag = True

print()

max_weight = 1
min_weight = 30000

for i in range(user_number):
    weight = randint(1, 30000)
    print(weight)

    if weight > max_weight:
        max_weight = weight
        max_count = i + 1
    elif weight < min_weight:
        min_weight = weight
        min_count = i + 1

print()

print(f"Итого, Ивану достался самый жирный арбуз с весом {max_weight}  под номером {max_count}, а теще, ну, самый компактный - {min_weight} под номером {min_count}")