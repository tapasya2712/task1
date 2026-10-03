import math


class Computation:
    

    def __init__(self):
        
        pass

    def Factorial(self, n: int) -> int:
        
        if n < 0:
            raise ValueError("Factorial is not defined for negative integers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def Sum(self, n: int) -> int:
        
        if n < 0:
            raise ValueError("Sum is not defined for negative integers.")
        return (n * (n + 1)) // 2

    def testPrim(self, n: int) -> bool:
        
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        # Check odd factors up to sqrt(n)
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def testPrims(self, a: int, b: int) -> bool:
        
        return math.gcd(a, b) == 1


# --- Instantiating and Testing the Class ---
if __name__ == "__main__":
    # 1. Instantiate the class using default constructor
    calc = Computation()

    # 2. Test Factorial()
    print("=== 1. Factorial Test ===")
    print(f"Factorial(5) = {calc.Factorial(5)}")   # 5! = 120
    print(f"Factorial(0) = {calc.Factorial(0)}")   # 0! = 1
    print(f"Factorial(7) = {calc.Factorial(7)}")   # 7! = 5040

    # 3. Test Sum()
    print("\n=== 2. Sum Test ===")
    print(f"Sum(5)   (1+2+3+4+5)   = {calc.Sum(5)}")   # 15
    print(f"Sum(10)  (1+...+10)   = {calc.Sum(10)}")  # 55
    print(f"Sum(100) (1+...+100) = {calc.Sum(100)}") # 5050

    # 4. Test testPrim()
    print("\n=== 3. Primality Test (testPrim) ===")
    test_numbers = [1, 2, 7, 12, 17, 25, 29]
    for num in test_numbers:
        print(f"testPrim({num:2d}) -> {calc.testPrim(num)}")

    # 5. Test testPrims()
    print("\n=== 4. Coprime Test (testPrims) ===")
    pairs = [(8, 15), (14, 28), (17, 19), (12, 25)]
    for a, b in pairs:
        is_coprime = calc.testPrims(a, b)
        print(f"testPrims({a:2d}, {b:2d}) -> {is_coprime} (GCD = {math.gcd(a, b)})")
