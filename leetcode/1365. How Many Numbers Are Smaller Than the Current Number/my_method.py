class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srtd_nums = sorted(nums)
        out_put = []
        for num in nums:
            out_put.append(srtd_nums.index(num))
        return out_put
        