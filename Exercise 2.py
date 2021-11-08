class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if not isinstance(other, (Rectangle, int, float)):
            return NotImplemented
        return self.width * self.height == other.width * other.height

    def __gt__(self, other):
        if not isinstance(other, (Rectangle, int, float)):
            return NotImplemented
        return self.width * self.height > other.width * other.height

    def __lt__(self, other):
        if not isinstance(other, (Rectangle, int, float)):
            return NotImplemented
        return self.width * self.height < other.width * other.height

    def __add__(self, other):
        if not isinstance(other, (Rectangle, int, float)):
            return NotImplemented
        return self.width * self.height + other.width * other.height

    def multiplication(self, n):
        return self.width * self.height * n


a = Rectangle(1, 3)
b = Rectangle(2, 2)
print(a < b)
print(a > b)
print(a == b)
print(b.multiplication(2))
print(a + b)