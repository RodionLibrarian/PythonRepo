def my_func():
    result = 0
    while True:
        list = input('Введите числа через пробел или "." для выхода: ').split()
        for i in range(len(list)):
            if list[i] == '.':
                return result
            else:
                try:
                    result += int(list[i])
                except ValueError:
                    print('Введите числа или "."!')
        print(result)


print(my_func())
