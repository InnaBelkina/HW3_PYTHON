# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X, 
# выводим все числа в отсортированном виде (по возрастанию)

# РЕШЕНИЕ БЕЗ УСЛОЖНЕНИЯ
lst1_len = int(input('Введите количество элементов в списке: '))
lst1 = []
for i in range(lst1_len):
    num = int(input('Добавим в список число: '))
    lst1.append(num)

x = int(input("Введите число X: "))
min_diff=abs(lst1[0] - x)
ans_i=0
for i in range(1,len(lst1)):
    if abs(lst1[i] - x) < min_diff:
        min_diff = abs(lst1[i]- x)
        ans_i=i

print(f"Ответ: {lst1[ans_i]}")

# РЕШЕНИЕ С УСЛОЖНЕНИЕМ
lst1_len = int(input('Введите количество элементов в списке: '))
lst1 = []
for i in range(lst1_len):
    num = int(input('Добавим в список число: '))
    lst1.append(num)

x = int(input("Введите число X: "))
min_diff=abs(lst1[0] - x)
ans_i=0
lst2=[]
for i in range(len(lst1)):
    if abs(lst1[i] - x) <= min_diff:
        min_diff = abs(lst1[i]- x)
        lst2.append(lst1[i])
if lst2[0] - lst2[1] !=  0:
    lst2.pop(0)

lst2.sort()
print(lst2)