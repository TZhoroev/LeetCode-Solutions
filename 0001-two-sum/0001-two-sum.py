class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d  ={num:index for index, num in enumerate(nums)}
        for idx in range(len(nums)-1):
            x = target - nums[idx]
            index = d.get(x, -1)
            if index!=-1 and index!=idx: return[idx, index]
    
        