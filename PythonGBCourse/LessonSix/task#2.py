class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, asph_mass, asph_thick):
        return round(self._length * self._width * asph_mass * asph_thick / 1000)


out = Road(20, 5000)
print(f'{out.mass(25, 5)} тонн асфальта')
