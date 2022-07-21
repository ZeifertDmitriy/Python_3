# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_nech(spisok):
    sum = 0
    for i in range(len(spisok)):
        if i % 2 == 1 :
            sum = sum + spisok[i]
    return sum

spisok = [1, 2, 3, 4, 53, 68]
print(spisok)
print(sum_nech(spisok))