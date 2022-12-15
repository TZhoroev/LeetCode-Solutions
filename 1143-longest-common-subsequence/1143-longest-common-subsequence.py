class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for char1 in text1:
            upper, diag_left = 0, 0
            for i,  char2 in enumerate(text2):
                upper, diag_left = dp[i + 1], upper
                dp[i + 1] = diag_left + 1 if char1 == char2 else max(dp[i], upper)
        return dp[-1]

