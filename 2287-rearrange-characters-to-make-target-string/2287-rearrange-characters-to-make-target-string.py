class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        S, T = Counter(s), Counter(target)
        res = float("inf")
        for char in T:
            if char in S:
                res = min(res, S[char]//T[char])
            else:
                return 0
        return res
                