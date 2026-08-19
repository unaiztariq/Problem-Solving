# Problem 1: Filter and Validate Matrix Rows
# Statement:
# You are given a 4x4 matrix. Check each row to ensure all values lie between 1 and 100.
# Then, filter out the rows where the sum of the elements is less than 150.
# Finally, return the valid and filtered rows sorted in descending order of their row sums.

def filter_validate_v1(a):
    b = []
    for i in a:
        for j in i :
            if i not in b:
                b.append(i)
            if j <1 or j >= 100 :
                b.remove(i) 
                break
            if sum(i) > 150:
                b.remove(i)
    return b


def filter_validate_v2(a):
    for rows in a[:]:
        for num in rows :
            if num <1 or num >= 100 :
                a.remove(rows)   
                break
    
        if sum(rows) > 150:
            a.remove(rows)
    return a


def filter_validate_optimized(a):
    b = []
    for row in a:
        if all(1 <= val < 100 for val in row):
            if sum(row) <= 150:
                b.append(row)
    return b

a = [
    [2, 7, 4, 1],
    [9, 5, 3, 8],
    [6, 0, 2, 4],
    [1, 80, 70, 30]
]

print(filter_validate_optimized(a))
