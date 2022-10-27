class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspace(s)==self.backspace(t)    
        
    def backspace(self, string):
        stack = []
        for char in string:
            if char=="#":
                if stack:
                    stack.pop()
            else: stack.append(char)
        return stack
        
        