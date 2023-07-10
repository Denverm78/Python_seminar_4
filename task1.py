""" Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки. """

def convert_str(str_for_convert):
    convert_list = str_for_convert.split()
    convert_list.sort()    
    len_max_str = len(max(convert_list, key=len))    
    for int, int_str in enumerate(convert_list):
        print(int+1, int_str.rjust(len_max_str))

user_str = input("Введите строку: ")
convert_str(user_str)
