rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('taskfour.txt', 'r') as file_obj:
    # content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('taskfour_upd.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
