class Solution:
    def decodeString(self, s: str) -> str:
        stack, current_num, current_string = [], "", ""
        for char in s:
            if char =="[":
                stack.append(current_string), stack.append(current_num)
                current_string, current_num = "", ""
            elif char =="]":
                num = stack.pop()
                st = stack.pop()
                current_string = st + int(num)*current_string
            elif char.isdigit(): current_num += char
            else: current_string += char
        return current_string
        