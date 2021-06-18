from abc import ABC, abstractmethod


class Textile(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return f'Суммарный объем ткани на пошив: {self.consumption + other.consumption:.05} кв.м.'


class Coat(Textile):
    def __init__(self, parameter):
        super().__init__(parameter)

    @property
    def consumption(self):
        print(f'Требуется ткани для пальто: {round(self.parameter / 6.5) + 0.5} кв.м.')
        return round(self.parameter / 6.5) + 0.5


class Costume(Textile):
    def __init__(self, parameter):
        super().__init__(parameter)

    @property
    def consumption(self):
        print(f'Требуется ткани для костюма: {(2 * self.parameter + 0.3) / 100:04} кв.м.')
        return (2 * self.parameter + 0.3) / 100


coat = Coat(50)
costume = Costume(181)
print(coat + costume)

