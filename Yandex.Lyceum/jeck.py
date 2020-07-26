all_tituls = []
for i in range(int(input())):
    word = input()
    tituls = ''
    while word != '*':
        tituls += word + ' '
        word = input()
    splitted = tituls.split()
    joined = '-'.join(splitted)
    all_tituls.append(joined)
str_tituls = ', '.join(all_tituls[-1::-1])
print(str_tituls)
