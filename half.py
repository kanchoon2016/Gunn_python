class RawFraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("addtional number fraction")
        if denominator == 0:
            raise ZeroDivisionError("fraction")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator

  
    def __add__(self, other):
        if not isinstance(other, RawFraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return RawFraction(num, den)


    def __sub__(self, other):
        if not isinstance(other, RawFraction):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return RawFraction(num, den)


    def __mul__(self, other):
        if not isinstance(other, RawFraction):
            return NotImplemented
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return RawFraction(num, den)
    
    def __truediv__(self, other):
        if not isinstance(other, RawFraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("ไม่สามารถหารด้วยเศษส่วนที่ตัวเศษเป็นศูนย์ได้")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return RawFraction(num, den)


# ตัวอย่างการใช้งาน
def main():
    f1 = RawFraction(1, 12)   
    f2 = RawFraction(5, 4)   
    print(f1+f2) 


if __name__ == "__main__":
    main()
