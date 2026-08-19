# Two-Sum: Given a list of integers nums and a target integer target, return a pair of indices (i, j)
# such that nums[i] + nums[j] == target. Assume exactly one solution exists and i != j.

# Input: A list of integers nums and an integer target.
# Output: A tuple of two indices.
# Example: nums = [2, 7, 11, 15], target = 9 -> output (0, 1) (because 2 + 7 = 9).

def two_sum(nums,target):
    skip = 1
    for num in nums:
        for num_index in range(0+skip,len(nums)):
            if  num + nums[num_index] == target:
                return (num,nums[num_index])
        skip +=1
    return  -1

print(two_sum([2, 7, 11, 15], 9))
