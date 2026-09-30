def print_table(n: int) -> None:
    print(f"Таблица умножения для числа {n}:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    number = 7
    print_table(number)