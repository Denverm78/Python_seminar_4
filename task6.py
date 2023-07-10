""" Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка. """

from random import randint

def summ_numbers(original_list, index1, index2):
    if index1 > index2:
        temp = index1
        index1 = index2
        index2 = temp
    if index1 < 0:
        index1 = 0
    if index2 > (len(original_list) - 1):
        index2 = len(original_list) - 1
    summ_number = sum(original_list[index1: index2 + 1])
    return summ_number

count = int(input("Введите количество чисел в списке: "))
random_list = []
for i in range(count):
    random_list.append(randint(1,99))
print("Исходный список: ")
print(random_list)
index_1 = int(input("Введите первый индекс: "))
index_2 = int(input("Введите второй индекс: "))
result_summ = summ_numbers(random_list, index_1, index_2)
print("Сумма чисел между переданными индексами равна", result_summ)