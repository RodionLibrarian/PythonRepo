def my_func(a, b, c):
    list = [a, b, c]
    min = list[1]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    list.remove(min)
    return sum(list)


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
print(my_func(a, b, c))
