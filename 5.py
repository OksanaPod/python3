# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


n = int(input('Введите число: '))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def negafibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return negafibonacci(n-2) - negafibonacci(n-1)

list = []
for i in range(0, n+1):
    list.append(fibonacci(i))
for i in range(1, n+1):
    list.insert(0, negafibonacci(i))

print(f'Cписок чисел Фибоначчи для числа {n}, в том числе для отрицательных индексов: \n{list}')