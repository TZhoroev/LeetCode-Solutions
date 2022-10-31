class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn, profit= float("-inf"), float("inf"), 0
        for price in prices:
            if price < mn: mn = mx = price
            elif price > mx: profit, mx = max(profit, price - mn), float("-inf")
        return profit