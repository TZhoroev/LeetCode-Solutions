class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, flips = 0, 0
        for char in s:
            if char =="1":
                ones +=1
            else:
                flips +=1
            flips = min(flips, ones)
        return flips

                
        
        