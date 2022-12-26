class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_n = mid_n = float("inf")
        for num in nums:
            if min_n >= num: min_n = num
            elif mid_n>=num: mid_n = num
            else: return True
        return False
                
        