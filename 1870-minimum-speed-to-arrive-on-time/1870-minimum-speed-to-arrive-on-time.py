class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right, ans = 1, 10**7, -1
        
        def helper(c_speed):
            t_hour = 0
            for d in dist[:-1]:
                t_hour += math.ceil(d/c_speed)
            t_hour += dist[-1]/c_speed
            return t_hour <= hour
            
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                right, ans = mid -1, mid
            else:
                left = mid + 1
        return ans