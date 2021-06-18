season_list = ['Зима', 'Весна', 'Лето', 'Осень']

month_number = int(input('Введите номер месяца: '))

if month_number in (12, 1, 2):
    print('Время года: ' + season_list[0])
elif month_number in (3, 4, 5):
    print('Время года: ' + season_list[1])
elif month_number in (6, 7, 8):
    print('Время года: ' + season_list[2])
else:
    print('Время года: ' + season_list[3])

season_dict = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
               9: 'Осень', 10: 'Осень', 11: 'Осень'}

month_number = int(input('Введите номер месяца: '))

print('Время года: ' + season_dict.get(month_number))
