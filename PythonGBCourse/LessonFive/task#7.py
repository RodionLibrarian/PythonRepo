import json
output_list = []
profit = {}
average = {}
all_profit = 0
average_profit = 0
i = 0
with open('taskseven.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            all_profit = all_profit + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = all_profit / i
        print(f'Средняя прибыль для {i} фирм равна: {average_profit:.2f}')
    else:
        print(f'Средняя прибыль - отсутсвует. Все работают в убыток')
    average = {'Средняя прибыль: ': round(average_profit)}
    output_list = [profit, average]
    print(f'Прибыль каждой компании - {output_list}')

with open('taskseven.json', 'w', encoding='utf-8') as write_js:
    json.dump(output_list, write_js, ensure_ascii=False)
    print(f'Создан файл с расширением json со следующим содержимым: {output_list}')
