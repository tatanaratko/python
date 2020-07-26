rows = int(input())
cols = int(input())
table = []
table = [[input() for col in range(cols)] for row in range(rows)]

for row in range(len(table)):
    print('\t'.join(table[row]))
