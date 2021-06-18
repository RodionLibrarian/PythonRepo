def make_list(**kwargs):
    return list(kwargs.values())


print(make_list(name=input('Enter first name: '), secname=input('Enter second name: '),
                birth_year=input('Enter birth year: '),
                live_town=input('Enter live town: '),
                email=input('Enter e-mail: '), phone=input('Enter phone number: ')))
