import math


class Circle:
   

    def __init__(self, a: float, b: float, r: float):
        
        self.a = a
        self.b = b
        self.r = r

    def Area(self) -> float:
        
        return math.pi * (self.r ** 2)

    def Perimeter(self) -> float:
        
        return 2 * math.pi * self.r

    def testBelongs(self, x: float, y: float) -> bool:
        
        distance_squared = (x - self.a) ** 2 + (y - self.b) ** 2
        return math.isclose(distance_squared, self.r ** 2)


# --- Demonstration & Testing ---
if __name__ == "__main__":
    # Create Circle C with center O(0, 0) and radius r = 5
    c = Circle(0, 0, 5)

    print("=== Circle Properties ===")
    print(f"Center O  : ({c.a}, {c.b})")
    print(f"Radius r  : {c.r}")
    print(f"Area      : {c.Area():.4f}")
    print(f"Perimeter : {c.Perimeter():.4f}")

    print("\n=== Point Membership Tests ===")
    # Point A(3, 4): (3-0)² + (4-0)² = 9 + 16 = 25 == 5² -> True
    print(f"Point A(3, 4) belongs to circle? {c.testBelongs(3, 4)}")

    # Point A(5, 0): (5-0)² + (0-0)² = 25 == 5² -> True
    print(f"Point A(5, 0) belongs to circle? {c.testBelongs(5, 0)}")

    # Point A(2, 2): (2-0)² + (2-0)² = 8 != 25 -> False
    print(f"Point A(2, 2) belongs to circle? {c.testBelongs(2, 2)}")
