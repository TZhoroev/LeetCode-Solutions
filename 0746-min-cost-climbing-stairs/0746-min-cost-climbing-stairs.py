class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        M = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            new = min(cost[i] + M[i-2], cost[i] + M[i-1])
            M.append(new)
        return min(M[-1], M[-2])    
        