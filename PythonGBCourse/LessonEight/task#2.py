class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def DivideByNull(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Деление на ноль недопустимо"


divider = input('Please enter the divider: ')
denominator = input('Please enter the denominator: ')
print(DivisionByNull.DivideByNull(int(divider), int(denominator)))
