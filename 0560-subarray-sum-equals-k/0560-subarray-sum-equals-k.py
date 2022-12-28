class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums, prefix_sum , ans = collections.defaultdict(int), 0, 0 
        prefix_sums[0] = 1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            key = prefix_sum - k
            if prefix_sums[key]: ans += prefix_sums[key]
            prefix_sums[prefix_sum] += 1
        return ans
