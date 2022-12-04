class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum, n = 0, len(nums) 
        min_abs_diff = float("inf")
        res = 0 
        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            c_diff = abs(right_sum//(n - i -1) - left_sum//(i+1))
            if c_diff < min_abs_diff:
                min_abs_diff = c_diff
                res = i
             
        return res if min_abs_diff <= sum(nums)//n else n-1
        
        