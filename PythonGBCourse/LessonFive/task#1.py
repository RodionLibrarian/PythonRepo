file = open('taskone.txt', 'w')
line = input('Enter text: ')
while line:
    file.writelines(line)
    line = input('Enter text: ')
    if not line:
        break

file.close()
file = open('taskone.txt', 'r')
content = file.readlines()
print(content)
file.close()
