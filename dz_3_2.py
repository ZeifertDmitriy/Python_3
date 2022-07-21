# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def proizv(spisok):
    pro = list()
    for i in range(len(spisok)):
        if len(spisok) % 2 == 0:
            if i > len(spisok) / 2:
                break
        else:
            if i == (len(spisok) // 2) + 1:
                break
        pro.append(spisok[i] + spisok[len(spisok) - 1 - i])
    return pro


spisok = [1, 2, 3, 4, 7, 9]
print(spisok)
print(proizv(spisok))
