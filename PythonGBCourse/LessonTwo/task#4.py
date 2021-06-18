instring = input('Введите строку: ')

work_list = instring.split(' ')
print(work_list)

for i in range(len(work_list)):
    if len(work_list[i]) > 10:
        print(f"{i + 1}-я строка: " + work_list[i][0:10])
    else:
        print(f"{i+1}-я строка: " + work_list[i])


