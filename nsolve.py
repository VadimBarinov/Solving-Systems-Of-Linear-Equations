from sympy import symbols, Eq, nsolve

# Определение переменных
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Определение системы уравнений
equations = [
    Eq(x1 - 4*x2 + 3*x3 + 7*x4, 4),
    Eq(-2*x1 + x2 - x3 + 3*x4, 6),
    Eq(4*x1 - 3*x2 + x3 + 5*x4, 2),
    Eq(-x1 + 2*x2 - x3 - x4, 4)
]

# Начальное предположение для численного решения
initial_guess = [0, 0, 0, 0]

# Нахождение численного решения
numerical_solution = nsolve(equations, (x1, x2, x3, x4), initial_guess)

# Вывод результатов
print("\nЧисленное решение:")
for i in range(numerical_solution.shape[0]):
    print(f"x{i+1} = {numerical_solution[i]}")
