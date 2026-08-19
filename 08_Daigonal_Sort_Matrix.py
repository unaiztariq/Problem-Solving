# Problem 2: Diagonal Sort with Range Check
# Statement:
# You are given a 5x5 matrix. Validate that all elements lie between 0 and 50.
# Then, extract both the primary and secondary diagonals.
# Sort both diagonals separately in ascending order, and return the sorted lists.

def diagonal_sort(list_2d55):
    pri_diagonal =[]
    sec_diagonal =[]
    pri_index = 0
    sec_index = 4
    for rows in list_2d55:
        if all( 0<num<=50 for num in rows):
            pri_diagonal.append(rows[pri_index])
            sec_diagonal.append(rows[sec_index])
            pri_index += 1
            sec_index -= 1
                
        else:
            raise ValueError("Invalid matrix, elements lie between 0 and 50.")

    return sorted(pri_diagonal), sorted(sec_diagonal)


matrix = [
    [2, 7, 4, 1,49],
    [9, 5, 34, 8,1],
    [6, 17, 4, 4,7],
    [1, 1, 7, 34,34],
    [21, 7, 4, 1,9]
]

pri, sec = diagonal_sort(matrix)
print(pri)
print(sec)
