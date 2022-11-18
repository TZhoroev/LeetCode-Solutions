class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n
        
        ans = 0
        i = 0
        while i + k <= n:
            if s[i:i + k] == s[i:i + k][::-1]:
                ans += 1
                i = i + k
            elif s[i:i + k + 1] == s[i:i + k + 1][::-1]:
                ans += 1
                i = i + k + 1
            else:
                i += 1
        
        return ans
        