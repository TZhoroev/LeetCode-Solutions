class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        for i, char in enumerate(palindrome[:n//2]):
            if char != "a": return palindrome[:i]+"a"+palindrome[i+1:]
        return palindrome[:-1]+"b" if n > 1 else ""
        