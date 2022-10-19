class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n
        a, b = 0, freq[1]
        for i in range(2, len(freq)):
            a, b = b,  max(freq[i] + a, b)
        return b
        