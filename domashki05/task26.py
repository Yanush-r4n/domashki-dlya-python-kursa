# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def pow(num: int, power: int):
    
    if power == 1:
        return num
    
    if power == 0:
        return 1
    
    number = num * pow(num, power - 1)

    return number

print(pow(3, 5))