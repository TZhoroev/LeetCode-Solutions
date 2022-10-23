from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        for item in range(len(nums)):
            if c[item+1]==0: a = item+1
            elif c[item+1]==2: b = item+1
        return[b, a]
        