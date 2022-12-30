class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}
        s = s.split()
        if len(s) != len(pattern): return False
        for letter, word in zip(pattern, s):
            if letter in d1 and d1[letter] != word: 
                return False
            else: d1[letter] = word
            if word in d2 and d2[word] != letter: 
                return False
            else: d2[word] = letter

        return True