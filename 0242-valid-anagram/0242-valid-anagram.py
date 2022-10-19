from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(t)
        if len(s)>=len(t):
            for item in d1:
                if d1[item]!=d2[item]:return False
        else:
            for item in d2:
                if d1[item]!=d2[item]:return False
        return True