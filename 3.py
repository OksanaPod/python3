# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

def find(my_list):
  min = 1
  max = 0
  for i in my_list:
    if (i - int(i)) <= min:
        min = round(i - int(i),2)
    if (i - int(i)) >= max:
        max = round(i - int(i),2)
  print(f'разница между максимальным и минимальным значением дробной части элементов', {max-min})

try:
  li = list(map(float,input('Введите числа через пробел:').split()))

  find(li)
except:
  print ('Введено не  число')