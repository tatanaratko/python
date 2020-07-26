str_quantity = input()
quantity = int(str_quantity[1:])

for i in range(quantity):
    string = input()
    comment_index = string.find('#')
    if comment_index != -1:
        string = string[:comment_index].rstrip()
    else:
        without_space = string.rstrip()
        string = without_space
    print(string)
