from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        d1, d2 = defaultdict(lambda:0), defaultdict(lambda:0)
        for a, b in zip(secret, guess):
            if a==b: bulls +=1
            else: 
                d1[a] += 1
                d2[b] += 1
        cows = sum([min(d1[char], d2[char]) for char in d2])
        return f"{bulls}A{cows}B"
        