my_list = [7, 5, 3, 3, 2]

while True:
    new_number = input('Введите новое число: ')
    if new_number == 'q':       # выход из цикла While (секретка)
        break
    else:
        new_number = int(new_number)
        my_list.append(new_number)
        my_list.sort(reverse=True)
        print('Новый рейтинг выглядит так: ' + str(my_list))

