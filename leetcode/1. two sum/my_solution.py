class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sliced_nums = nums[(i + 1):len(nums)]
            for j in range(len(sliced_nums)):
                if (nums[i] + sliced_nums[j]) == target:
                    return [i, i+j+1]
                    break

