items_list = []

number_of_items = int(input('Введите количество товаров: '))

for i in range(number_of_items):
    name_of_item = input(f'Введите наименование {i + 1}-го товара: ')
    price_of_item = int(input(f'Введите цену {i + 1}-го товара: '))
    amount_of_item = int(input(f'Введите количество {i + 1}-го товара: '))
    count_of_item = input(f'Введите единицы {i + 1}-го товара: ')

    temp_dict = {'название': name_of_item, 'цена': price_of_item, 'количество': amount_of_item, 'ед': count_of_item}
    temp_tuple = (i + 1, temp_dict)
    items_list.append(temp_tuple)

print(items_list)

tmp_name_list = []
tmp_price_list = []
tmp_amount_list = []
tmp_count_list = []

for i in range(number_of_items):
    tmp_name_list.append(items_list[i][1].get('название'))
    tmp_price_list.append(items_list[i][1].get('цена'))
    tmp_amount_list.append(items_list[i][1].get('количество'))
    tmp_count_list.append(items_list[i][1].get('ед'))

statistics_dict = {'название': tmp_name_list, 'цена': tmp_price_list,
                   'количество': tmp_amount_list,
                   'ед': list(set(
                       tmp_count_list))}  # только для 'ед' сделал определение повторяющихся значений, так как считаю,
# что для остальных значений это важно
print(statistics_dict)
