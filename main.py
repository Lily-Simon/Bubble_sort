'''Практическое задание итоговой аттестации'''
'''Создание программы на Python, выполняющей сортировку методом пузырька'''
#!usr/bin/env/python3
# -*- coding: utf-8 -*-
from random import randint
import time

# Ввод числа
def nask(amin=20, amax=1000):
    # проверка корректности аргументов и получение информации от пользователя
    if 20 < amin < 1000 and amin < amax:
        amin = amin
    else:
        amin = 20
    if 20 < amax < 1000 and amax > amin:
        amax = amax
    else:
        amax = 1000
    user_count = input(f'Укажите количество чисел для сортировки от {amin} до {amax}: ')
    # проверка ввода пользователя
    while user_count.isdigit() == False or amax < int(user_count)  or  int(user_count) < amin:
        if user_count.isdigit() == False:
            print(f'Нужно указывать только целые числа! Повторите ввод!')
            user_count = input(f'Укажите количество чисел для сортировки от {amin} до {amax}: ')
        elif amax < int(user_count)  or  int(user_count) < amin:
            print(f'Вводимое число не может быть меньше указанного минимального порога {amin} или больше максимального порога {amax}')
            user_count = input(f'Укажите количество чисел для сортировки от {amin} до {amax}: ')
    else:
        user_count_check = int(user_count)
        return user_count_check

# Список со случайными числами, длина которого равна числу, указанному пользователем
l1 = []
for i in range(nask()):
    l1.append(randint(10000, 99999))
# print(f'Сгенирированный список: {l1}')

# Cортировка
time_start = time.perf_counter()
def bub_sort(g):
    for k in range(len(g) - 1):
        for j in range(len(g) - k - 1):
            if g[j] > g[j + 1]:
                g[j], g[j + 1] = g[j + 1], g[j]
    return g
time_end = time.perf_counter()
time_proc = time_end - time_start

l1_sort = bub_sort(l1)
# print(f'Отсортированный список: {l1_sort}')

# Вывод программы
print(f'Количество чисел в списке: {len(l1_sort)}')

print(f'Процессорное время, которое было затрачено на сортировку: {time_proc:.3f} сек') #round(time_proc, 3)

print(f'Сумма 10 максимальных чисел отсортированного списка: {sum(l1_sort[len(l1_sort) - 10::])}')

print(f'Сумма 10 минимальных чисел отсортированного списка: {sum(l1_sort[:10])}')

