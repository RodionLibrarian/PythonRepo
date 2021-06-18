from itertools import count

cnt = 0

for el in count(int(input('Введите стартовое число '))):
    if cnt < 100:
        print(el)
        cnt += 1
    else:
        break

from itertools import cycle

list = ['Hello', 42, False]
for el in cycle(list):
    if cnt < 100:
        print(el)
        cnt += 1
    else:
        break
