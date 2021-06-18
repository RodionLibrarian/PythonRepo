list = [109, 234, 532, 32, 43, 12, 54, 54, 23, 12]
new_list = [el for num, el in enumerate(list) if list[num] > list[num - 1]]

print(f'Исходный список {list}')
print(f'Новый список {new_list}')