class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}: {self.position}'

    def get_total_income(self):
        return f"""Доход составляет: {self._income.get('wage') + self._income.get('bonus')}"""


SH = Position('Sherlock', 'Holmes', 'Detective', 400, 15)
print(SH.get_full_name())
print(SH.get_total_income())

DW = Position('John', 'Watson', 'Doctor', 300, 55)
print(DW.get_full_name())
print(DW.get_total_income())