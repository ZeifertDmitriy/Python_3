# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def raz(spisok):
    min = spisok[0] % 1
    max = spisok[0] % 1
    for i in range(len(spisok)):
         if spisok[i] % 1 > max:
            max = spisok[i] % 1
         if spisok[i] % 1 == 0:
            continue  
         if spisok[i] % 1 < min:
            min = spisok[i] % 1
    return round(max - min, 2)

spisok = [1.1, 1.2, 3.1, 5, 10.01]
print(spisok)
print(raz(spisok))