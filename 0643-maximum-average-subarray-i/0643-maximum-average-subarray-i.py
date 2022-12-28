class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == len(nums): return sum(nums)/k
        total = max_sum = sum(nums[: k])
        for i in range(len(nums) - k):
            # print(total, nums[i + k], nums[i] )
            total += nums[i + k] - nums[i]
            max_sum = max(max_sum, total)
        return max_sum/k
            