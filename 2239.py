from typing import List

# Nums list
nums = [-4,-2,1,4,8]

def findClosestNumber(nums:List[int]) -> int:
    # Creating a new array for sorted
    new_nums = []
    for i in nums:
        new_nums.append(abs(i))
    new_nums.sort()
    
    return new_nums[0]

print(findClosestNumber(nums))
