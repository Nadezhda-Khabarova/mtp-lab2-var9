def recursive_sum(n: int) -> int:
    """Рекурсивно вычисляет сумму чисел от 1 до n."""
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

if __name__ == "__main__":
    number = 10
    print(f"Сумма чисел от 1 до {number} равна: {recursive_sum(number)}")