my_file = open('tasktwo.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('tasktwo.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле: {len(content)}')
my_file = open('tasktwo.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов в {i + 1} - ой строке: {len(content[i]) - 1}')
my_file = open('tasktwo.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Всего слов: {len(content)}')
my_file.close()
