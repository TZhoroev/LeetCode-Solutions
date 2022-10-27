class Solution:
    def isValid(self, s: str) -> bool:

        result = []
        for char in s:
            match char:
                case "(":
                    result.append(0)
                case ")":
                    if len(result)==0 or result.pop()!=0: return False  
                case "{":
                    result.append(1)
                case "}":
                    if len(result)==0 or result.pop()!=1: return False       
                case "[":
                    result.append(2)
                case "]":
                    if len(result)==0 or result.pop()!=2: return False 
        if result:
            return False
        else:
            return True