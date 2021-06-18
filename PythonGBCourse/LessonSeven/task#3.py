class cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return cell(self.quantity - other.quantity)
        else:
            return 'Вычитание невозможно!'

    def __mul__(self, other):
        return cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.quantity // cells_in_row):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


firstbatch = cell(54)
secondbatch = cell(12)
print(firstbatch)
print(secondbatch)
print(firstbatch + secondbatch)
print(firstbatch - secondbatch)
print(secondbatch - firstbatch)
print(f'Порядок 1: \n{firstbatch.make_order(5)}')
print(f'Порядок 2: \n{secondbatch.make_order(3)}')
print(firstbatch / secondbatch)
