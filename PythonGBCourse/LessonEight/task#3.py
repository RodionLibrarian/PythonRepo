class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Please enter a number: '))
                self.my_list.append(val)
                print(f'Current list: {self.my_list} \n ')
            except ValueError:
                print(f"Error: Unacceptable type!")
                YorN = input(f'Try again Y/N: ')

                if YorN in ['Y', 'y', 'yes', 'yeah']:
                    print(try_except.my_input())
                elif YorN in ['N', 'n', 'no', 'nope']:
                    return f'Ending cycle.'
                else:
                    return f'Ending cycle.'


try_except = Error(1)
print(try_except.my_input())
