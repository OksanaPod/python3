# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def find_proizv(list):
    new_list = []
    for i in range(len(list) // 2):
        new_list.append(list[i] * list[len(list) - i - 1])
    if len(list)%2 !=0:
        a = list[len(list)//2]
        list[len(list) // 2] = a * a
        new_list.append(list[len(list)//2])
    print(new_list)

try:
    data = list(map(int, input('Введите числа через пробел').split()))
    print(data)
    find_proizv(data)

except:
    print(f'Error')