class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0: return max(nums)
        max_sum = curr_max = min_sum = curr_min = nums[0] 
        for i in range(1, len(nums)): 
            curr_max, curr_min = max(nums[i], curr_max + nums[i]), min(nums[i], curr_min + nums[i]) 
            max_sum, min_sum = max(max_sum, curr_max), min(min_sum, curr_min) 
        return max(max_sum, sum(nums) - min_sum)
        