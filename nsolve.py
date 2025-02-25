from sympy import symbols, Eq, nsolve

# Определение переменных
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Определение системы уравнений
equations = [
    Eq(x1 + x2 + x3 + x4, 0),
    Eq(5*x1 - 3*x2 + 2*x3 - 8*x4, 1),
    Eq(3*x1 + 5*x2 + x3 + 4*x4, 0),
    Eq(4*x1 + 2*x2 + 3*x3 + x4, 3)
]

# Начальное предположение для численного решения
initial_guess = [0, 0, 0, 0]

# Нахождение численного решения
numerical_solution = nsolve(equations, (x1, x2, x3, x4), initial_guess)

# Вывод результатов
print("\nЧисленное решение:")
for i in range(numerical_solution.shape[0]):
    print(f"x{i+1} = {numerical_solution[i]}")
