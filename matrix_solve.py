from sympy import symbols, Matrix

# Функция применения матричного метода для решения системы линейных уравнений
def matrix_solve(A, B):
    # Вычисление определителя главной матрицы
    det_A = A.det()
    # Проверка на случай, если определитель главной матрицы равен нулю
    if det_A == 0:
        raise ValueError("Определитель матрицы коэффициентов равен нулю.")
    # Находим обратную матрицу
    A_inv = A.inv()
    # Находим решение
    solutions = A_inv * B


    return solutions

# Матрица коэффициентов системы уравнений
A = Matrix([
    [1, -2, 3],
    [2, -3, -4],
    [2, -5, 1],
])
# Вектор значений
B = Matrix([2, -5, -2])


try:
    # Вызов функции для решения системы уравнений матричным методом
    solutions = matrix_solve(A, B)
    # Вывод результатов
    print("Решение матричным методом:")
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")
except ValueError as e:
    print(e)
