class Solution:
    def findLHS(self, nums: List[int]) -> int:
        C = Counter(nums)
        longest_harmony = 0
        for key, val in C.items():
            if C[key+1]:
                longest_harmony = max(longest_harmony, C[key] + C[key+1])
        return longest_harmony

