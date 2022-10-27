from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, result = len(s), len(p), []
        p, i = Counter(p), 0
        while i < n - m +1:
            if i==0:
                initial = Counter(s[:m])
            else:
                initial[s[i-1]]-=1
                initial[s[i+m-1]]+=1
            if len(initial - p)==0:result.append(i)
            i+=1
        return result
                
        