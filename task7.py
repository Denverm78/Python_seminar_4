""" Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами 
и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, 
верните истину, а если хотя бы одна убыточная — ложь. """

def profit_or_loss(original_dict):
    for i in original_dict.values():
        if sum(i) <= 0:
            return False
    return True

dict_companies = {"Буревестник" : [100000, 150000, -20000, 15000, -30000, 50000], 
                  "Эдельвейс" : [200000, -50000, -10000, 5000, 10000], 
                  "Буратино" : [30000, 35000, -20000, -10000, 40000, -20]}
result = profit_or_loss(dict_companies)
if result == True:
    print("Все компании прибыльные")
else:
    print("Хотя бы одна из компаний - убыточная")