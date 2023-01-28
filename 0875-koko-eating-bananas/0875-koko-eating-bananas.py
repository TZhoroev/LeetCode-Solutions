class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, sum(piles)
        def helper(speed):
            if speed == 0: return False
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / speed)
            return hours <= h
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if helper(mid):
                right, ans = mid -1, mid 
            else:
                left = mid + 1
        return ans