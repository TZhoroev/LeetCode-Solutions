class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0:-1}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            current_sum %= k
            if current_sum in prefix_sum and i - prefix_sum[current_sum]>1: return True
            if current_sum not in prefix_sum: 
                prefix_sum[current_sum] = i
        return False
        