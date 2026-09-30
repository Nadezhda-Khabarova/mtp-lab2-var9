def gcd(a: int, b: int) -> int:
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

if __name__ == "__main__":
    num1, num2 = 48, 18
    print(f"НОД чисел {num1} и {num2} равен: {gcd(num1, num2)}")