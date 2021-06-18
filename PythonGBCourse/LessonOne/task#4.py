number = int(input("Enter integer number: "))

max_num = number % 10
number = number // 10

while number != 0:
    comp_num = number % 10
    if comp_num > max_num:
        max_num = comp_num
    number = number // 10

print(max_num)
