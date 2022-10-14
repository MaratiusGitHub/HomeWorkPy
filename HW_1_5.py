# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
import random


def print_massive(array):
    for i in range(len(array)):
        print(array[i])


a = int(input('Введите количество строк двумерного массива: '))
b = int(input('Введите количество столбцов двумерного массива: '))

mas_2din = []
for i in range(a):
    temp = []
    for j in range(b):
        temp.append(round(random.random() * 100))
    mas_2din.append(temp)

print_massive(mas_2din)

for i in range(a):
    for j in range(b):
        for x in range(a):
            for y in range(b):
                if mas_2din[x][y] > mas_2din[i][j]:
                    count = mas_2din[i][j]
                    mas_2din[i][j] = mas_2din[x][y]
                    mas_2din[x][y] = count

print()
print_massive(mas_2din)
