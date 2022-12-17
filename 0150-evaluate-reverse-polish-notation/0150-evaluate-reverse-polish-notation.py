class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                char = stack.pop() + stack.pop()
            elif char == "-":
                char = - stack.pop() + stack.pop()
            elif char == "*":
                char = stack.pop() * stack.pop()
            elif char == "/":
                char = 1 / stack.pop() * stack.pop()
            stack.append(int(char))
        return stack[-1]