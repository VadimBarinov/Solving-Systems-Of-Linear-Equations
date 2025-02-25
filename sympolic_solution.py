from sympy import symbols, Eq, solve

# Определение переменных
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Определение системы уравнений
equations = [
    Eq(x1 + x2 + x3 + x4, 0),
    Eq(5*x1 - 3*x2 + 2*x3 - 8*x4, 1),
    Eq(3*x1 + 5*x2 + x3 + 4*x4, 0),
    Eq(4*x1 + 2*x2 + 3*x3 + x4, 3)
]

# Решение системы символьно
symbolic_solution = solve(equations, (x1, x2, x3, x4))

# Вывод решения
print("Символьное решение:")
for i in symbolic_solution:
    print(f"{i} = {symbolic_solution.get(i)}")
