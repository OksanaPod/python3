# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
try:
 x = int(input('Введите число: '))
 list = []
 while x > 0:
         y = x%2
         list.append(y)
         x = x//2
 for i in range(len(list)//2):
     tmp = list[i]
     list[i] = list[len(list) - i - 1]
     list[len(list) - i - 1] = tmp
 print (*list)

except:
  print ('Введено не число')