from functools import reduce


def func(el_p, el):
    return el_p * el


print(f'Список из четных чисел {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов {reduce(func, [el for el in range(99, 1001) if el % 2 == 0])}')
