from sympy import Matrix, pprint


def print_row_reduced_matrix(matrix):
    print("Ступенчатая матрица:")
    pprint(matrix)


# Определение расширенной матрицы [A|B]
augmented_matrix = Matrix([
    [1, 1, -2, 6],
    [2, 3, -7, 16],
    [5, 2, 1, 16],
])

# Выполнение приведения матрицы к ступенчатому виду
row_reduced_matrix, _ = augmented_matrix.rref()

# Вызов функции для вывода ступенчатой матрицы
print_row_reduced_matrix(row_reduced_matrix)

# Вывод результатов
print('\nРешение системы:')
for i in range(row_reduced_matrix.shape[0]):
        print(f"x{i+1}: {row_reduced_matrix[i, -1]}")
