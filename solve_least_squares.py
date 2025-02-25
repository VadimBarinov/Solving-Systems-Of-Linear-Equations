from sympy import symbols, Matrix

# Определение матрицы коэффициентов
coefficients_matrix = Matrix([
    [1, 2, -1, 1],
    [2, 5, 1, 7],
    [-3, -10, 0, 6],
    [4, 10, 2, 15],
])

# Определение матрицы значений
constants_matrix = Matrix([-6, -4, -5, -7])

# Решение системы с помощью метода наименьших квадратов
least_squares_solution = coefficients_matrix.solve_least_squares(constants_matrix)

# Вывод решения
print("\nРешение методом наименьших квадратов:")
for i in range(least_squares_solution.shape[0]):
    print(f"x{i+1} = {least_squares_solution[i]}")
