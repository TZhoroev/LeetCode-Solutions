class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        nums = [-1] + nums
        N = len(nums)
        dp = [inf for x in range(N)]
        dp[0] = 0
        i = 0
        while i < N:
            #c = Counter()
            c = [0 for x in range(N-1)]
            curr = 0
            for j in range(i+1, N):
                c[nums[j]] += 1
                if c[nums[j]] > 2:
                    curr += 1
                elif c[nums[j]] == 2:
                    curr += 2
                tmp = dp[i] + curr + k
                if dp[j] > tmp:
                    dp[j] = tmp
            i += 1
                    
        return dp[-1]
        