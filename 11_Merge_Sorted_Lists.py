
# Merge Sorted Lists: Given two lists of integers
# that are already sorted in ascending order, merge them into a single sorted list.

# Input: Two sorted lists of integers, A and B.
# Output: A single list containing all elements of A and B, in ascending order.
# Example: A = [1, 4, 7], B = [2, 3, 6] -> output [1, 2, 3, 4, 6, 7].


def merge(list_1,list_2):
    merge_list = []
    index_1 = 0
    index_2 = 0



    while True:
        if list_1[index_1] <= list_2[index_2]:
            merge_list.append(list_1[index_1])
            index_1 +=1
        elif list_1[index_1] > list_2[index_2]:
            merge_list.append(list_2[index_2])
            index_2+=1
        if index_2 == len(list_2):
            while index_1<len(list_1):
                merge_list.append(list_1[index_1])
                index_1 +=1
            break
            
        elif index_1 == len(list_1):
            while index_2<len(list_2):
                merge_list.append(list_2[index_2])
                index_2 +=1
            break
    return merge_list

a = [1, 4, 7]
b = [2, 3, 6]
print(merge(a,b))
