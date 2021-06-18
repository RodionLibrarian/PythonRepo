firstday = int(input("Пробежал в первый день: "))
result = int(input("Хочу добиться: "))
daycount = 1

print(f"{daycount}-й день: {firstday:0.2f}")

while firstday < result:
    firstday = firstday * 1.1
    daycount += 1
    print(f"{daycount}-й день: {firstday:0.2f}")

print(f'Количество дней для результата: {daycount}')
