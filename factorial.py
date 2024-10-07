class Factorial:
    def __init__(self, n: int):
        self.n = n

    def calculate(self) -> int:
        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        return result

if __name__ == "__main__":
    fact = Factorial(5)
    print(fact.calculate())  # Output: 120
