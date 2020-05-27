class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array = []
        for indx, num in enumerate(nums):
            target_array.insert(index[indx], num)
        return target_array