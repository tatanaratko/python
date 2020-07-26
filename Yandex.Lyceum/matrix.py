def matrix(n=1, m=1, a=0):
    matrix = []
    for i in range(n):
        matrix.append([])
        if m == 1 and n != 1:
            for j in range(n):
                matrix[i].append(a)
        elif m != 1:
            for j in range(m):
                matrix[i].append(a)
        else:
            matrix = [[0]]
    return matrix
