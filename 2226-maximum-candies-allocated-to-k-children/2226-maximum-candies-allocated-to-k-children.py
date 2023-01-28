class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        def helper(c_max):
            if c_max == 0:
                return True
            c_candies = 0
            for candie in candies:
                c_candies += candie//c_max
            return c_candies >= k
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if helper(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans 
        