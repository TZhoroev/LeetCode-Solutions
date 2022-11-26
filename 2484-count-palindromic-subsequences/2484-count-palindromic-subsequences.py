class Solution:
    def countPalindromes(self, s: str) -> int:         
        n, ans = len(s), 0
        ans = 0 
        for i in range(10): 
            for j in range(10):   
                x = str(i) + str(j) + '#' + str(j) + str(i) 
                dp = [0, 0, 0, 0, 0, 1]          
                for k in range(n): 
                    for l in range(5): 
                        if s[k] == x[l] or l == 2: 
                            dp[l] += dp[l + 1]                  
                ans += dp[0] % int(1e9 + 7)
        
        return ans % int(1e9 + 7)