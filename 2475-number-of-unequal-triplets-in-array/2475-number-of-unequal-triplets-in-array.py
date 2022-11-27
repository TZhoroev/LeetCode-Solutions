class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if len(set([nums[i], nums[j], nums[k]])) == 3:
                        count +=1
        return count
        
        