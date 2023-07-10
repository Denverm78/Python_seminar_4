""" Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии """

from random import randint

def sort_numbers(user_list):
    for i in range(len(user_list)):
        for j in range(len(user_list) - 1 - i):
            if user_list[j + 1] < user_list[j]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    return user_list

count = int(input("Введите количество чисел в списке: "))
random_list = []
for i in range(count):
    random_list.append(randint(1,99))
print("Исходный список: ")
print(random_list)
result = sort_numbers(random_list)
print("Отсортированный список: ")
print(result)
