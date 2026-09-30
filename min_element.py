def find_min_element(numbers: list[float | int]) -> float | int | None:
    if not numbers:
        return None
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    # Тестовые данные
    test_list = [15, 4, 23, 8, 2, 99, 1]
    print(f"Список: {test_list}")
    print(f"Минимальный элемент: {find_min_element(test_list)}")