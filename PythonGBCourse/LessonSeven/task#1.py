class Matrix:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_one)):
            for j in range(len(self.list_two[i])):
                matrix[i][j] = self.list_one[i][j] + self.list_two[i][j]

        return str('\n'.join([' '.join([str(j) for j in i]) for i in matrix]))


def str_filter(list):
    new_list = []
    for v in list:
        try:
            int(v)
            new_list.append(int(v))
        except ValueError:
            continue
    return new_list


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]), end=" ")
        print()


list_one = []
list_two = []

for i in range(1):
    tmp_list = []
    for j in range(3):
        tmp_list.append(str_filter(input(f'Введите {j + 1}-й ряд 1-ой матрицы через пробел: ').split()))
    list_one = tmp_list

for i in range(1):
    tmp_list = []
    for j in range(3):
        tmp_list.append(str_filter(input(f'Введите {j + 1}-й ряд 2-ой матрицы через пробел: ').split()))
    list_two = tmp_list

my_matrix = Matrix(list_one, list_two)

print(f'Cуммарная матрица:\n{my_matrix.__add__()}')
