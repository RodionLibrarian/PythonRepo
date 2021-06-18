def title_fucn(text):
    new_str = ''
    for i in range(len(text)):
        if i == 0:
            new_str += text[i].upper()
        else:
            new_str += text[i]

    return new_str


print(title_fucn('lorem'))


def title_fucn2(text):
    list = text.split()
    new_str = ''
    for i in range(len(list)):
        list[i] = title_fucn(list[i])
    new_str = ' '.join(list)
    return new_str


print(title_fucn2('lorem ipsum dolor sit amet'))
