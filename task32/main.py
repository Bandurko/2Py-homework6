# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

def index(nums, min, max):
    list = []
    for i in range(len(nums)):
        if nums[i] <= max and nums[i] >= min:
            list.append(i)
    return list

from random import randint

lenght_nums = int(input('Введите длину массива (списка): '))
nums = list(randint(1, 10) for i in range(lenght_nums))

print(*nums)

min = int (input('Введите минимальное значение заданного диапазона: '))
max = int (input('Введите максимальное значение заданного диапазона: '))

print(*index(nums, min, max))
