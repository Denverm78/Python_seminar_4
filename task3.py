"""  Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно. """

def create_dict(original_str):
    new_list = original_str.split()   
    max_element = int(max(new_list))
    min_element = int(min(new_list))
    print(max_element, min_element)
    new_dict = {}
    for i in range(min_element, max_element+1):
        new_dict[chr(i)] = i
    return(new_dict)


user_str = input("Введите строку из двух чисел через пробел: ")
result_dict = create_dict(user_str)
print(result_dict)