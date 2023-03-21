class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, c_zeros = 0, 0
        for num in nums:
            if num:
                c_zeros = 0
            else:
                res += 1 + c_zeros
                c_zeros += 1
        return res
                    
            
        