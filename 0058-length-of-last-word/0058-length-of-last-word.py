class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()[-1]
        return len(string.strip())
        
        