""" Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце. """
            
def change_variablis():
    temp = globals()  
    changed_var = {}
    for key, value in temp.items():
        if key.endswith('s') and key != 's':
            changed_var[key[:-1]] = temp[key]
            temp[key] = None
    for key, value in changed_var.items():
        temp[key] = value          

var1s = "one"
var2 = "two"
var3s = "three"
var4 = "four"
s = "five"
print(var1s, var2, var3s, var4, s)
change_variablis()
print(var1s, var2, var3s, var4, s, var1, var3) # Проверяем, создались ли новые переменные
# print(globals())