from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        queue = deque(s.replace(' ',''))
        return self.helper(queue) 
    def helper(self, q):       
        res = 0       
        num = 0
        sign = '+'     
        while q:
            x = q.popleft()
            if x == '(':
                num = self.helper(q) # go to next level
            elif x.isdigit():
                num = num * 10 + int(x)
            if not x.isdigit() or not q:
                if sign =='+': res += num
                elif sign =='-': res -= num
                sign = x
                num = 0
            if x == ')':
                break
        return res
        
                
        
        