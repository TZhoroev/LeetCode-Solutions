from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        stack.append((")", -1))
        result = 0
        for i, char in enumerate(s):
            match char:
                case "(":
                    stack.append((char, i))
                case ")":
                    if stack[-1][0] == "(":
                        stack.pop()
                        result = max(result, i - stack[-1][1])
                    else: stack.append((char, i))   
                        
        return result                   
            
        