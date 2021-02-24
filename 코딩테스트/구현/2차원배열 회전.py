a = [[1,2,3],[4,5,6],[7,8,9]]

def rotate_90_degree(a): 
    row_num = len(a)
    column_num = len(a[0])

    result = [[0] * row_num for _ in range(column_num)]

    for i in range(row_num):
        for j in range(column_num):
            result[j][row_num-1-i] = a[i][j]

    print(result)

rotate_90_degree(a)

def rotate_180_degree(a): 
    row_num = len(a)
    column_num = len(a[0])

    result = [[0] * row_num for _ in range(column_num)]

    for i in range(row_num):
        for j in range(column_num):
            result[row_num-1-i][column_num-1-j] = a[i][j]

    print(result)

rotate_180_degree(a)

def rotate_270_degree(a): 
    row_num = len(a)
    column_num = len(a[0])

    result = [[0] * row_num for _ in range(column_num)]

    for i in range(row_num):
        for j in range(column_num):
            result[row_num-1-j][i] = a[i][j]

    print(result)

rotate_270_degree(a)
