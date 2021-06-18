class Date:
    def __init__(self, dmy_format):
        self.day_month_year = str(dmy_format)

    @classmethod
    def extract(cls, dmy_format):
        my_date = []

        for i in dmy_format.split('-'):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Date is OK!'
                else:
                    return f'Wrong year!'
            else:
                return f'Wrong month!'
        else:
            return f'Wrong day!'

    def __str__(self):
        return f'Current date: {Date.extract(self.day_month_year)}'


today = Date('2 - 10 - 2020')
print(today)
print(Date.validation(36, 11, 2022))
print(today.validation(11, 13, 2011))
print(Date.extract('15 - 6 - 2011'))
print(today.extract('16 - 08 - 2020'))
print(Date.validation(23, 1, 1997))
