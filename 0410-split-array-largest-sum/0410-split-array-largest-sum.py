class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        def helper(total):
            if max(nums) > total: return False
            c_sum, n_subarray =  0, 1
            for num in nums:
                if c_sum + num > total:
                    c_sum = num
                    n_subarray += 1
                else:
                    c_sum += num
            return n_subarray  <= k
        left, right = 0, sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
        
    