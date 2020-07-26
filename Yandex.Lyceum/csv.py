cols_quantity = int(input())
cols = []
for i in range(cols_quantity):
    col = input()
    cols.append(col.split(','))

coordinate_quantity = int(input())

for j in range(coordinate_quantity):
    coordinate = input().split(',')
    word_row, word_col = int(coordinate[0]), int(coordinate[1])
    word = cols[word_row][word_col]
    print(word)
