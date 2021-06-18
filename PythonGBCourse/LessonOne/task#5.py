profit = int(input("Введите выручку: "))
loss = int(input("Введите убыток: "))

if profit > loss:
    print(f"Выручка больше убытка на {profit - loss}")
    rentabprecents = ((profit - loss) / profit) * 100
    rentabinue = rentabprecents * profit / 100

    print(f"Рентабельность фирмы в у.е. = {rentabinue:0.2f}")
    print(f"Рентабельность фирмы в процентах = {rentabprecents:0.2f} %")

    employees = input("Количество сотрудников в фирме: ")
    profitonemployees = (profit - loss) / int(employees)

    print(f'Прибыль на сотрудника составляет: {profitonemployees:0.2f}')
else:
    print("Прибыли нет")

