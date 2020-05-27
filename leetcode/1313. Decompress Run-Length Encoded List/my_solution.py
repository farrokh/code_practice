class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out_put = []
        i = 0
        while i < (len(nums) - 1):
            freq = nums [i]
            val = nums[i + 1]
            j = 0
            while j < freq:
                out_put.append(val)
                j += 1
            i += 2
        return out_put