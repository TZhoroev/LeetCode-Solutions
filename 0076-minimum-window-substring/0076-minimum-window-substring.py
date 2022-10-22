from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc, w = Counter(t), Counter()
        left, ans = 0, ""
        for index, char in enumerate(s):
            w[char] = w.get(char, 0) +1
            while w>=tc:
                if ans == "" or index-left<len(ans):
                    ans = s[left: index +1]
                w[s[left]] -= 1
                left += 1
        return ans
                

        