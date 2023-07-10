""" Напишите функцию для транспонирования матрицы  """

from random import randint

def trans_matrix(original_matrix):
    result_matrix = [[0 for j in range(len(original_matrix))] for i in range(len(original_matrix[0]))]
    for i in range(len(original_matrix)):
        for j in range(len(original_matrix[0])):
            result_matrix[j][i] = original_matrix[i][j]
    return result_matrix

def print_matrix(matrix_for_print):
    for i in range(len(matrix_for_print)):
        for j in range(len(matrix_for_print[i])):
            print(matrix_for_print[i][j], end='  ')
        print()

n = int(input("Введите размер матрицы n: "))
m = int(input("Введите размер матрицы m: "))
user_matrix = [[randint(1,9) for j in range(m)] for i in range(n)]
print()
print("Исходная матрица: ")
print(user_matrix)
print()
print_matrix (user_matrix)
print()
result = trans_matrix(user_matrix)
print("Транспонированная матрица: ")
print(result)
print()
print_matrix(result)