class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for string in arr:
            if len(set(string)) == len(string):
                string = set(string)
                for p_string in dp[:]:
                    if not string & p_string:
                        dp.append(string | p_string)
        return max(len(string) for string in dp)
        