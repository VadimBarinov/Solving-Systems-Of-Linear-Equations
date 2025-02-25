from sympy import symbols, Matrix

# Определение матрицы коэффициентов
coefficients_matrix = Matrix([
    [1, 1, 1, 1],
    [5, -3, 2, -8],
    [3, 5, 1, 4],
    [4, 2, 3, 1]
])

# Определение матрицы значений
constants_matrix = Matrix([0, 1, 0, 3])

# Решение системы с помощью метода наименьших квадратов
least_squares_solution = coefficients_matrix.solve_least_squares(constants_matrix)

# Вывод решения
print("\nРешение методом наименьших квадратов:")
for i in range(least_squares_solution.shape[0]):
    print(f"x{i+1} = {least_squares_solution[i]}")
