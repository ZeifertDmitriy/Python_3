# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# def seach(spisok,str):
#     for i in range(len(spisok)):
#         if str in spisok[i]:
#             print(spisok[i])

# spisok = ['1', '2', '3', '4', '53', '68']
# print(spisok)
# str = input('Введите значение для поиска: ')
# seach(spisok,str)


# Напишиете программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
# def vhozdenie(spisok,str):
#     num_v = 0
#     for i in range(len(spisok)):
#         if str == spisok[i]:
#             num_v +=1
#         if num_v == 2:
#             print(i)
#             break
#     if num_v < 2:
#         print('-1')

# spisok = ['1', '2', '3', '2', '3', '68']
# print(spisok)
# str = input('Введите значение для поиска: ')
# vhozdenie(spisok,str)


# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time

def gen(kol):
    strk = ''
    i = 0
    while i < kol:
    #for i in kol - 1:
        a = str(time.time())
        strk.append(a[-2])
        i += 1

kol = int(input('Введите количество знаков: '))
print(gen(kol))
