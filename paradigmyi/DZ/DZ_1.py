# Задача 1: Подсчет суммы четных чисел от 1 до N.
# Напишите программу, используя цикл, которая находит сумму 
# всех четных чисел в диапазоне от 1 до заданного числа N.

# def sum_even_imperative(numbers):
#     sum = 0
#     for num in numbers:
#         if num % 2 == 0:
#             sum = sum + num
#     return sum

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_even_imperative(numbers))


# Задача 2: Поиск наименьшего числа в списке.
# Напишите программу, которая находит наименьшее 
# число в заданном списке с помощью цикла.

def sum_even_imperative(numbers):
    # min = 0
    index = 0
    max = 0
    for min in numbers:
        if max > min:
            max = min
            # index + 1
        # if max > min:
        #     index + 1
    return min

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_imperative(numbers))
