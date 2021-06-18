def summary():
    try:
        with open('taskfive.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неверный тип данных (Введите целые числа). Ошибка ввода-вывода')


summary()
