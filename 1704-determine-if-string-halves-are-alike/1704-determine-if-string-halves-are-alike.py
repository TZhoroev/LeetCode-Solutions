class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        n = len(s)//2
        count = 0
        for i in range(n):
            if s[i] in vowels:
                count +=1
        for i in range(n, 2*n):
            if s[i] in vowels:
                count -=1
        return count==0
        
        