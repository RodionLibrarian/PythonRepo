class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Z1 + Z2 is equal: ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Z1 * Z2 is equal: ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(3, -4)
z_2 = ComplexNumber(3, -6)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)