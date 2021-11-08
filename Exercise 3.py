class ProperFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if not isinstance(other, (ProperFraction, int, float)):
            return NotImplemented
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __gt__(self, other):
        if not isinstance(other, (ProperFraction, int, float)):
            return NotImplemented
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other):
        if not isinstance(other, (ProperFraction, int, float)):
            return NotImplemented
        return self.numerator / other.denominator < other.numerator / other.denominator

    def __add__(self, other):
        if not isinstance(other, (ProperFraction, int, float)):
            return NotImplemented
        return f'{self.numerator * other.denominator + self.denominator * other.numerator}/'\
               f'{self.denominator * other.denominator}'

    def __mul__(self, other):
        if not isinstance(other, (ProperFraction, int, float)):
            return NotImplemented
        return f'{self.numerator * other.numerator}/{self.denominator * other.denominator}'


fractional = ProperFraction(1, 8)
fractional1 = ProperFraction(3, 7)
print(fractional + fractional1)
print(fractional * fractional1)
print(fractional > fractional1)