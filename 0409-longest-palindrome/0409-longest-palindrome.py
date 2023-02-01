class Solution:
    def longestPalindrome(self, s: str) -> int:
        S, res, cond = Counter(s), 0, False
        for value in S.values():
            res += (value // 2) * 2
            if value % 2:
                cond = True
        return res + 1 if cond else res
        