# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101
# 3 -> 11
# 2 -> 10

def dvoich(number):
    dv = ''
    while number > 0:
        dv = str(number % 2) +dv
        number = number //2
    return dv

number = int(input('Введите десятичное число: '))
print(dvoich(number))