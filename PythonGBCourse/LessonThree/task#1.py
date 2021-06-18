def division(firstnum, secnum):
    output = firstnum / secnum
    return output


firstnum = int(input('Введите делимое: '))
secnum = int(input('Введите делитель: '))

while secnum == 0:
    print('Пожалуйста введите делитель отличный от нуля!')
    secnum = int(input('Введите делитель: '))

print('Частное равно:', division(firstnum, secnum))

