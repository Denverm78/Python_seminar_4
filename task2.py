""" Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию """

def create_list(str_for_create):
    new_list = list(str_for_create)
    code_list = []
    for i in new_list:
        if ord(i) not in code_list:
            code_list.append(ord(i))
    code_list.sort(reverse =True)
    return(code_list)    

user_str = input("Введите строку: ")
result_list = create_list(user_str)
print("Уникальные коды символов введенной строки: ", result_list)