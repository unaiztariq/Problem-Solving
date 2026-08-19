# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.

def longest_consecutive(strarr, k):
    if k <= 0 or not strarr:
        return ""

    first =  "".join(strarr[0:k])
    second =  "".join(strarr[1:k+1])
    if len(first)>=len(second):
        greatest = (first)   
    elif len(first)<len(second):
        greatest = (second)
    for i in range(2,len(strarr)-1):
        challenger =  "".join(strarr[i:k+i])
        if len(greatest)< len(challenger):
            greatest = challenger
    return greatest

star = ["tree", "foling", "trashy", "blue", "abcdefgk", "uvwxyzk"]
print(longest_consecutive(star, 2))
