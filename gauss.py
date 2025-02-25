from sympy import Matrix, pprint


def print_row_reduced_matrix(matrix):
    print("Ступенчатая матрица:")
    pprint(matrix)


# Определение расширенной матрицы [A|B]
augmented_matrix = Matrix([
    [1, 1, 1, 1, 0],
    [5, -3, 2, -8, 1],
    [3, 5, 1, 4, 0],
    [4, 2, 3, 1, 3]
])

# Выполнение приведения матрицы к ступенчатому виду
row_reduced_matrix, _ = augmented_matrix.rref()

# Вызов функции для вывода ступенчатой матрицы
print_row_reduced_matrix(row_reduced_matrix)

# Вывод результатов
print('\nРешение системы:')
for i in range(row_reduced_matrix.shape[0]):
        print(f"x{i+1}: {row_reduced_matrix[i, -1]}")
