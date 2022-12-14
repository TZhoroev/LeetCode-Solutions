from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for index in range(len(s)):
            if c[s[index]]==1: return index
        return -1
        