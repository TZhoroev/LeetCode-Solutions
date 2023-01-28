class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right, ans = 1, max(nums), max(nums)
        
        def helper(penalty):
            ops = 0
            for num in nums:
                ops += math.ceil(num/penalty) - 1
            return ops <= maxOperations
        
        while left<= right:
            mid = (left + right) // 2
            if helper(mid):
                right, ans = mid - 1, mid
            else:
                left = mid + 1
        return ans
        