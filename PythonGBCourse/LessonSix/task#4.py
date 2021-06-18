class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self, direction):
        return f'{self.name} is turned {direction}'

    def show_speed(self):
        return f'{self.name} speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed {self.speed} is forbidden for {self.name} car'
        else:
            return f'Speed {self.speed} is okay for {self.name} car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed {self.speed} is forbidden for {self.name} car'
        else:
            return f'Speed {self.speed} is okay for {self.name} car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def if_police(self):
        if self.is_police:
            return f'{self.name} car is the police car!'
        else:
            return f'{self.name} car is not the police car!'


mazda_car = TownCar(50, 'Blue', 'Mazda CX7', False)
lambo_car = SportCar(120, 'Red', 'Lamborghini 9/11', False)
audi_car = WorkCar(80, 'Yellow', 'Audi A8', False)
ford_car = PoliceCar(100, 'White', 'Ford Focus', True)

print(mazda_car.go())
print(mazda_car.stop())
print(mazda_car.turn('left'))
print(mazda_car.show_speed())

print(lambo_car.go())
print(lambo_car.stop())
print(lambo_car.turn('right'))
print(lambo_car.show_speed())

print(audi_car.go())
print(audi_car.stop())
print(audi_car.turn('right'))
print(audi_car.show_speed())

print(ford_car.go())
print(ford_car.stop())
print(ford_car.turn('left'))
print(ford_car.show_speed())
print(ford_car.if_police())