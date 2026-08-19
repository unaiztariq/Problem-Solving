# Given two positive integers m (width) and n (height), fill a two-dimensional list (or array)
# of size m-by-n in the following way:
# All the elements in the first and last row and column are 1.
# All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
# All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
# And so on …

def matrix_sequence_v1(m,l):
    fabricated_list= [0 for _ in range(m)]
    main_list= []

    for i in range(1,(l//2)+1):
        for j in range(i-1,w+1-i):
            fabricated_list[j]=i
    for i in range((l//2)+1,0,-1):
        for j in range(i-1,w+1-i):
            fabricated_list[j]=i
    return fabricated_list


def matrix_sequence_v2(m,n):
    array = []
    dic={}

    half = n//2+1
    base =[ 1 for _ in range(m)]
    for i in range (1,half-1):
        row = f"row{i}"
        a=i-1
    
        for j in range(a,m-a):
            base[j]=i
        dic[row]=base.copy()
    con = half
    for i in range(half-1,n+1):
        row = f"row{i}"
        a=con-1
        for j in range(a,m-a):
            base[j]=con
        dic[row]=base.copy()

        con -=1

    for key,value in dic.items():
        array+= value,
    return array

print(matrix_sequence_v2(13,14))
