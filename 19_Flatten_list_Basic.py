def flatten_list_basic(a):
    b = []
    for i in range (0,len(a)):
        b += a[i]
    return b

a = [
   [2,7,4,1],
   [8,7,3,1],
   [3,9,4,1],
   [1,6,0,1]
]

print(flatten_list_basic(a))
