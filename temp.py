from typing import List

nums = [2,7,11,15] #[3,2,4] #[3,3]
target = 9 #6 #6


def twoSum(nums: List[int], target: int) -> List[int]:
    index = 0
    while index in range(len(nums) - 1):
        if nums[index] + nums[index+1] == target:
            return [index, index+1]
        else:
            index += 1

print(twoSum(nums,target))