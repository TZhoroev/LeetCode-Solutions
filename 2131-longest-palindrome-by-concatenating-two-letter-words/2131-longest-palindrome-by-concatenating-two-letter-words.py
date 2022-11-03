from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d, count = defaultdict(lambda: 0), 0
        for x in words:
            if d[x[::-1]]: 
                count +=4
                d[x[::-1]] -= 1
            else: d[x] += 1
        for word, num in d.items():
            if num and word[0]==word[1]:
                count+=2
                return count
        return count
            
        