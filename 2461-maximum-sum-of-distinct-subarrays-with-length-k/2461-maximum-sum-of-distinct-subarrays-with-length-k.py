class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sub_array_k = Counter(nums[:k-1])
        sum_k = sum(nums[:k-1])
        max_sum = 0
        for i in range(len(nums) - k + 1):
            sub_array_k[nums[i + k -1]] += 1
            sum_k += nums[i + k -1]
            if len(sub_array_k) == k:
                max_sum = max(max_sum, sum_k)
            sub_array_k[nums[i]] -= 1
            if sub_array_k[nums[i]] == 0:
                del sub_array_k[nums[i]]
            sum_k -= nums[i]
        return max_sum


