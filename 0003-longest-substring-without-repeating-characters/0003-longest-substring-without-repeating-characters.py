class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        max_sub = 0
        for i, char in enumerate(s):
            if char in used and start<=used[char]:
                start = used[char]+1
            else:
                max_sub = max(max_sub, i-start+1)
            used[char] = i
        return max_sub     
        