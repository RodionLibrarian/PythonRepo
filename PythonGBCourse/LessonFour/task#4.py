list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_list = [el for el in list if list.count(el) < 2]
print(new_list)