# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import re

def sum_odd_index(data):
    s = 0
    for i in range(len(data)):
        if i % 2 != 0:
           s += data[i]
    print(f"Сумма равна: {s}")
try:
 data = list(map(int,input('Введите числа через пробел').split()))
 print(data)
 sum_odd_index(data)

except:
 print(f'Пожалуйста, введите именно  число ')