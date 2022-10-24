class Solution:
    def rob(self, nums: List[int]) -> int:
        c, p = 0, 0
        for num in nums:
            p, c = c, max(num + p, c)
        return c
            
        