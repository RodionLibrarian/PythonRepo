list = []
elements = int(input('Пожалуйста введите количество элементов в списке: '))

for i in range(elements):
    list.append(int(input('Введите число: ')))

print(list)

for i in range(len(list)):
    if i % 2 == 0 and i != len(list) - 1:
        tmp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = tmp

print(list)