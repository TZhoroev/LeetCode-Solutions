class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, c_zeros = 0, 0
        for num in nums:
            if num:
                c_zeros = 0
            else:
                c_zeros += 1
                res += c_zeros
        return res
                    
            
        