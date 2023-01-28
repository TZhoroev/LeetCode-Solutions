class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right =  1, sum(batteries) // n
        
        def helper(n_hours):
            c_sum = 0
            for t in batteries:
                c_sum += t if t < n_hours else n_hours
            return c_sum >= n*n_hours
        while left <= right:
            mid = (left + right)//2
            if helper(mid):
                left, ans = mid + 1, mid
            else:
                right = mid - 1
        return ans
        