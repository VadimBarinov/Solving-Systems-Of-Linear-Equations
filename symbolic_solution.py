from sympy import symbols, Eq, solve

# Определение переменных
x1, x2, x3 = symbols('x1 x2 x3')

# Определение системы уравнений
equations = [
    Eq(x1 - 2*x2 + 3*x3, 2),
    Eq(2*x1 - 3*x2 - 4*x3, -5),
    Eq(2*x1 - 5*x2 + x3, -2),
]

# Решение системы символьно
symbolic_solution = solve(equations, (x1, x2, x3))

# Вывод решения
print("Символьное решение:")
for i in symbolic_solution:
    print(f"{i} = {symbolic_solution.get(i)}")
