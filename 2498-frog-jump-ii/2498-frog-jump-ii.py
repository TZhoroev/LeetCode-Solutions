class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[1] - stones[0])
        prev = stones[1]
        ans = 0
        for i in range(2, len(stones)):
            curr = abs(stones[i] - stones[i - 1])
            ans = max(ans, curr + prev)
            prev = curr
        return ans        