# Implement the function unique_in_order which takes as argument a sequence and
# returns a list of items without any elements with the same value next 
# to each other and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]

def unique_in_order(seq):
    li = []
    for i in range(0,len(seq)-1):
        if seq[i]==seq[i+1]:
            continue
        li.append(seq[i])
    li.append(seq[len(seq)-1])
    return li

print(unique_in_order('ABBCcAD'))
