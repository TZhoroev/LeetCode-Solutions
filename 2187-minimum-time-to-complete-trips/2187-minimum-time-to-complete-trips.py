class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, totalTrips * min(time)
        ans = right
        
        def helper(c_time):
            trips = 0
            for t in time:
                trips += c_time//t
            return trips >= totalTrips
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                ans, right = mid, mid - 1
            else:
                left = mid + 1
        return ans
        
        