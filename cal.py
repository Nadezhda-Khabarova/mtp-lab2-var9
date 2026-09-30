def calculate(a: float, b: float, operator: str) -> float | str:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Ошибка: деление на ноль!"
        return a / b
    else:
        return "Ошибка: неизвестная операция!"

if __name__ == "__main__":
    # Тесты калькулятора
    print("10 + 5 =", calculate(10, 5, '+'))
    print("10 / 0 =", calculate(10, 0, '/'))
    print("4 * 8 =", calculate(4, 8, '*'))
    print("10 % 2 =", calculate(10, 2, '%'))