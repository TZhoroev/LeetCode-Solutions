class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 0, max(quantities)
        def helper(amount):
            if amount == 0: return False
            n_stores = 0
            for q in quantities:
                n_stores += math.ceil(q/amount)
            return n_stores <= n
        while left <= right:
            mid = (right + left) // 2
            if helper(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans if ans else -1