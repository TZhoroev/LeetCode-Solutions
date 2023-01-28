class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days > len(weights):
            return -1
        def helper(total):
            if max(weights) > total: return False
            c_sum, n_subarray =  0, 1
            for num in weights:
                if c_sum + num > total:
                    c_sum = num
                    n_subarray += 1
                else:
                    c_sum += num
            return n_subarray  <= days
        left, right = 0, sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans