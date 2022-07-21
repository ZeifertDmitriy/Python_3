# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(number):
    fib_1 = 0
    fib_2 = 1
    fib_result = [1, 0, 1]
    for i in range(2, number):
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        fib_result.append(fib_2)
        fib_result.insert(0, ((- 1) ** (i + 1)) * fib_2)
    return fib_result

number = 9
print(fib(number))