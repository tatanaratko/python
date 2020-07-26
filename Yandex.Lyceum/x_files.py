def print_document(pages):
    pages_to_print = []
    x_file = 'Напечатано без купюр'
    for i in range(len(pages)):
        if 'Секретно' not in pages[i]:
            print(pages[i])
        else:
            x_file = 'Дальнейшие материалы засекречены'
            break
    print(x_file)
