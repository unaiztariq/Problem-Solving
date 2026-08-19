def transpose(matrix):
    transpose_matrix = [[] for _ in range(len(matrix[0])) ]
    for i in range(0,len(matrix)):
        for j in range(0,len(transpose_matrix)):
            transpose_matrix[j].append(matrix[i][j])

    return transpose_matrix

m = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25] 
     ]

print(transpose(m))
