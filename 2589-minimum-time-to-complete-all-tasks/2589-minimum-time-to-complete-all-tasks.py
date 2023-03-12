class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.append([10**9+1, 10**9+1, 1])
        tasks.sort(key=lambda x:x[0])
        res, q = 0, []
        for [s, e, d] in tasks:
            while q and q[0][0] + res < s :
                if q[0][0]+res >= q[0][1]: heapq.heappop(q)
                else : res += min(q[0][1], s) - (q[0][0]+res)
            heapq.heappush(q, [e-d+1-res, e+1])
        return res







