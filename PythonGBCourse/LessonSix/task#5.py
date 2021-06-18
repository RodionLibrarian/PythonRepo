class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы держите {self.title}. Запуск отрисовки ручкой!'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы держите {self.title}. Запуск отрисовки карандашом!'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы держите {self.title}. Запуск отрисовки маркером!'


pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())
