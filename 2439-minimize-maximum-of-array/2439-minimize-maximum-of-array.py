class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left, right, ans = 1, max(nums), max(nums)
        
        def helper(c_min):
            rem = 0
            for num in nums[::-1]:
                num += rem
                if num <= c_min:
                    rem = 0
                else:
                    rem = num - c_min
            return rem == 0
            
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                ans, right = mid, mid - 1
            else:
                left = mid + 1
        return ans
        