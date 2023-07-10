"""  Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление. """

def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        try:
            temp = hash(value)
            result_dict[value] = key
        except TypeError:
            result_dict[str(value)] = key
            
    return result_dict

result = create_dict(one=1, user_str="user_str", user_set=set([1,2]), user_frozenset=frozenset([3,4]), user_list=[5, 6, 7], user_tuple=(34, 56, 67))
print("Итоговый словарь: ") 
print(result)