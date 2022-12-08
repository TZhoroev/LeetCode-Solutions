class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        max_number = ""
        while len(nums) > 0:
            curr_max = "0"
            for num in nums:
                if num + curr_max > curr_max + num:
                    curr_max = num
            max_number += curr_max
            nums.remove(curr_max)
        return max_number if max_number[0]!="0" else "0"
                
        