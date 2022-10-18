class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        elif len(nums)==2: return max(nums)
        def rob1(nums):
            c, p = 0, 0
            for num in nums:
                p, c = c, max(num + p, c)
            return c
        return max(rob1(nums[1:]), rob1(nums[:-1]))
        