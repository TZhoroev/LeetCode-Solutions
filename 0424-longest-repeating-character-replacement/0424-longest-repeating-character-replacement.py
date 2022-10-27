from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d, length = defaultdict(lambda:0), 0
        for index, char in enumerate(s):
            d[char] += 1
            if length + 1 - max(d.values()) <=k: 
                length +=1
            else: d[s[index - length]] -= 1
        return length
        
        