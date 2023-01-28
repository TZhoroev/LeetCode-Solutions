class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        if threshold < len(nums): return -1
        
        
        def helper(divisor):
            c_sum = 0
            for num in nums:
                c_sum += math.ceil(num/divisor)
            return c_sum <= threshold
        
        ans = -1
        while left <= right:
            mid = (right + left)//2
            if helper(mid):
                ans, right = mid, mid - 1 
            else:
                left = mid + 1
        return ans
        